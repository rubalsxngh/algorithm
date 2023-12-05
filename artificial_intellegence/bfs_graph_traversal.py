
import collections


class Bfs:

    def __init__(self):
        self.output = []

    def bfs(self, adj, start_node, visited):
        q = collections.deque()
        q.append(start_node)

        while q:
            node = q.popleft()
            self.output.append(node)
            visited[node] = 1

            for nodex in adj[node]:
                if visited[nodex] == -1:
                    visited[nodex] = 1
                    q.append(nodex)


def main():
    '''
    let's look at the sample input
    input graph:
    V, E= 4, 4
    0->1,2
    1->0
    2->0
    3->1,2

    output:
    should contain all the vertices in output list in any order.
    '''
    V, E = map(int, input().split())
    adj = [[] for x in range(V)]

    for x in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    visited = [-1 for x in range(V)]
    bfs_instance = Bfs()
    for i in range(V):
        if visited[i] == -1:
            bfs_instance.bfs(adj, i, visited)

    print(bfs_instance.output)


if __name__ == '__main__':
    main()
