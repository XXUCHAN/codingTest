import heapq
from collections import Counter
def solution(n, edges):
    answer = 0
    m = 0
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append((v, 1))
        graph[v].append((u, 1))

    distances = [float('inf')] * (n + 1)

    start_node = 1
    distances[start_node] = 0

    queue = []
    heapq.heappush(queue, (distances[start_node], start_node))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for next_node, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))

    valid_distances = [d for d in distances if d != float('inf') and d != 0]
    max_dist = max(valid_distances)
    answer = valid_distances.count(max_dist)
    return answer
