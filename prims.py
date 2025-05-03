import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))
    
    def prim_mst(self):
        mst = []  
        visited = [False] * self.V
        min_heap = [(0, 0, -1)] 
        total_cost = 0
        
        while min_heap:
            weight, u, parent = heapq.heappop(min_heap)
            
            if visited[u]:
                continue
            
            visited[u] = True
            total_cost += weight
            
            if parent != -1:
                mst.append((parent, u, weight))
            
            for next_weight, v in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (next_weight, v, u))
        
        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in mst:
            print(f"{u} - {v}: {weight}")
        print(f"Total Cost of MST: {total_cost}")
        

total_vertices = int(input("Enter the number of vertices: "))
g = Graph(total_vertices)
edges = int(input("Enter the number of edges: "))

for _ in range(edges):
    while True:
        try:
            u, v, weight = map(int, input("Enter edge (u, v, weight): ").split())
            if u < 0 or v < 0 or weight < 0:
                print("Please enter non-negative integers.")
                continue
            g.add_edge(u, v, weight)
            break  
        except ValueError:
            print("Invalid input! Please enter three integers separated by spaces.")


g.prim_mst()
