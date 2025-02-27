def solve_tsp(G):
    n = len(G)
    visited = [False] * n
    path = []
    
    # Start at the first node
    current_node = 0
    path.append(current_node)
    visited[current_node] = True
    
    # Traverse the nodes using the nearest neighbor heuristic
    for _ in range(n - 1):
        nearest_neighbor = None
        min_distance = float('inf')
        
        for neighbor in range(n):
            if not visited[neighbor] and G[current_node][neighbor] != 0 and G[current_node][neighbor] < min_distance:
                nearest_neighbor = neighbor
                min_distance = G[current_node][neighbor]
        
        current_node = nearest_neighbor
        visited[current_node] = True
        path.append(current_node)
    
    # Return to the starting node to complete the tour
    path.append(0)
    
    return path

G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0]
]

path = solve_tsp(G)
print("Path taken:", path)