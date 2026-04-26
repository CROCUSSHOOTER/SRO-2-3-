import heapq
# Асфальт = 1, Песок = 3, Грязь = 5
robot_map = {
    'Start': {'A': 1, 'B': 3},
    'A': {'Start': 1, 'C': 5, 'D': 1},
    'B': {'Start': 3, 'D': 3, 'E': 5},
    'C': {'A': 5, 'Goal': 1},
    'D': {'A': 1, 'B': 3, 'Goal': 5},
    'E': {'B': 5, 'Goal': 1},
    'Goal': {'C': 1, 'D': 5, 'E': 1}
}

def dijkstra(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        (cost, current, path) = heapq.heappop(queue)
        
        if current in visited:
            continue
        
        path = path + [current]
        visited.add(current)
        
        if current == goal:
            return cost, path
            
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
                
    return float("inf"), []
cost, path = dijkstra(robot_map, 'Start', 'Goal')
print(f"Минимальная энергия: {cost}")
print(f"Оптимальный путь: {' -> '.join(path)}")
