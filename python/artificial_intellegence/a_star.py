import heapq
import random

class Astar:

    def __init__(self):
        self.cost = 0
    

    def astar(self, adj, start_node, goal, visited, distance, huerestic):
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
                    new_cost = current_cost + neighbor_cost+ huerestic[neighbor]
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
    since heurestic function is random, I can't predict path.
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
    total_sum_distances = sum(sum_distances)
    heurestic= [0 for x in range(V)]
    sum_distances = [sum(edge[0] for edge in edges) for edges in adj]
    for i in range(len(heurestic)):
        if i!=end:
            heurestic[i]= random.randint(1, total_sum_distances)


    astar_instance = Astar()

    print(astar_instance.ucs(adj, st, end, visited, distance, heurestic))



if __name__ == '__main__':
    main()
