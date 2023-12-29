import heapq


class Ucs:

    def __init__(self):
        self.cost = 0

    def ucs(self, adj, start_node, goal, visited, distance):
        q = [(0, start_node)]

        while q:
            current_cost, node = heapq.heappop(q)

            if visited[node] == 1:
                continue

            visited[node] = 1

            if node == goal:
                return current_cost

            for neighbor_cost, neighbor in adj[node]:
                if visited[neighbor] == -1:
                    new_cost = current_cost + neighbor_cost
                    if new_cost < distance[neighbor]:
                        distance[neighbor] = new_cost
                        heapq.heappush(q, (new_cost, neighbor))

        return float('inf')


def main():
    '''
    let's look at the sample input
    input graph:
    V, E= 4, 4
    0->1 1
    0->2 5
    1->3 1
    2->3 5

    st, end= 0, 3

    output:
    2 0->1->3
    '''
    V, E = map(int, input().split())
    adj = [[] for x in range(V)]

    for x in range(E):
        u, v, dist = map(int, input().split())
        adj[u].append([dist, v])
        adj[v].append([dist, u])

    st, end = map(int, input().split())

    visited = [-1 for x in range(V)]
    distance = [float('inf') for x in range(V)]
    ucs_instance = Ucs()

    print(ucs_instance.ucs(adj, st, end, visited, distance))



if __name__ == '__main__':
    main()
