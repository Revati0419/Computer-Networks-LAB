import heapq

class RouterOSPF:
    def __init__(self, router_id):
        self.router_id = router_id
        self.neighbors = {}  # Dictionary {neighbor_id: cost}

    def add_link(self, neighbor, cost):
        self.neighbors[neighbor.router_id] = cost
        neighbor.neighbors[self.router_id] = cost

    def dijkstra(self, network):
        unvisited = {router.router_id: float('inf') for router in network.values()}
        unvisited[self.router_id] = 0
        visited = {}
        pq = [(0, self.router_id)]  # Priority queue, starting with itself

        while pq:
            current_dist, current_router_id = heapq.heappop(pq)
            if current_router_id in visited:
                continue
            visited[current_router_id] = current_dist

            for neighbor_id, cost in network[current_router_id].neighbors.items():
                neighbor_router = network[neighbor_id]
                if neighbor_id not in visited:
                    new_dist = current_dist + cost
                    if new_dist < unvisited[neighbor_id]:
                        unvisited[neighbor_id] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor_id))

        return visited


# Example simulation
r1 = RouterOSPF(1)
r2 = RouterOSPF(2)
r3 = RouterOSPF(3)
r4 = RouterOSPF(4)

# Define the network topology
r1.add_link(r2, 10)
r1.add_link(r3, 15)
r2.add_link(r4, 20)
r3.add_link(r4, 30)

# Simulate the OSPF process
network = {1: r1, 2: r2, 3: r3, 4: r4}
for router in network.values():
    print(f"Router {router.router_id} shortest paths: {router.dijkstra(network)}")
