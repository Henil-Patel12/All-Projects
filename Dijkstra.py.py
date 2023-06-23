import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current);                
        for neighbor, ncost in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + ncost, neighbor))
    return visited

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2, 'E': 4},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 2, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1},
}

print(dijkstra(graph, 'A'))