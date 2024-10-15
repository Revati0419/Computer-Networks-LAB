class RouterRIP:
    def __init__(self, router_id):
        self.router_id = router_id
        self.routing_table = {router_id: 0}  # Distance to itself is 0

    def receive_routing_table(self, neighbor_table):
        for dest, dist in neighbor_table.items():
            if dest not in self.routing_table or self.routing_table[dest] > dist + 1:
                self.routing_table[dest] = dist + 1  # RIP increments by 1 (hop count)

    def send_routing_table(self):
        return self.routing_table


# Example simulation
r1 = RouterRIP(1)
r2 = RouterRIP(2)
r3 = RouterRIP(3)

# Simulating initial exchange of routing information
r1.receive_routing_table(r2.send_routing_table())
r1.receive_routing_table(r3.send_routing_table())
r2.receive_routing_table(r1.send_routing_table())
r2.receive_routing_table(r3.send_routing_table())
r3.receive_routing_table(r1.send_routing_table())
r3.receive_routing_table(r2.send_routing_table())

print(f"Router 1's routing table: {r1.routing_table}")
print(f"Router 2's routing table: {r2.routing_table}")
print(f"Router 3's routing table: {r3.routing_table}")
