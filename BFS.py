from queue import Queue

def get_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    e = int(input("Enter number of edges: "))
    
    for _ in range(e):
        u, v = input("Enter edge (u v): ").split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # Remove for directed graph

    return graph

def bfs(graph, start):
    visited = set()
    q = Queue()
    q.put(start)
    
    print("BFS Traversal:", end=" ")
    while not q.empty():
        node = q.get()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.put(neighbor)
    print()

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        print("DFS Traversal:", end=" ")
    
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    if start == list(graph.keys())[0]:
        print()

# Driver code
graph = get_graph()
start_node = input("Enter the starting node: ")

bfs(graph, start_node)
dfs(graph, start_node)
