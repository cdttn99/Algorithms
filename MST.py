import heapq

def Prims(G):
    num_vertices = len(G)
    selected = [False] * num_vertices
    mst_edges = []
    edge_queue = []
    
    # Start with vertex 0
    selected[0] = True
    
    # Add all edges from vertex 0 to the priority queue
    for j in range(num_vertices):
        if G[0][j] != 0:
            heapq.heappush(edge_queue, (G[0][j], 0, j))
    
    # While there are edges in the queue
    while edge_queue:
        weight, u, v = heapq.heappop(edge_queue)
        
        if not selected[v]:
            selected[v] = True
            mst_edges.append((u, v, weight))
            
            for j in range(num_vertices):
                if G[v][j] != 0 and not selected[j]:
                    heapq.heappush(edge_queue, (G[v][j], v, j))
    
    return mst_edges


input_graph = [
    [0, 8, 5, 0, 0, 0, 0],
    [8, 0, 10, 2, 18, 0, 0],
    [5, 10, 0, 3, 0, 16, 0],
    [0, 2, 3, 0, 12, 30, 14],
    [0, 18, 0, 12, 0, 0, 4],
    [0, 0, 16, 30, 0, 0, 26],
    [0, 0, 0, 14, 4, 26, 0]
]

output = Prims(input_graph)
print(output)