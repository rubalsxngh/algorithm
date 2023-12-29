
class Dfs:

    def __init__(self):
        self.output = []

    def dfs(self, adj, start_node, visited):
        self.output.append(start_node)
        visited[start_node] = 1

        for x in adj[start_node]:
            if visited[x] == -1:
                self.dfs(adj, x, visited)


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
    dfs_instance= Dfs()
    for i in range(V):
        if visited[i] == -1:
            dfs_instance.dfs(adj, i, visited)
    
    print(dfs_instance.output)


if __name__ == '__main__':
    main()
