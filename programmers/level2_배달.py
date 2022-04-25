from collections import deque

def solution(N, road, K):
    answer = 0
    maximum = int(1e9)
    graph = [[] for g in range(N+1)]
    
    for rd in road:
        graph[rd[0]].append((rd[1], rd[2]))  # vill, time
        graph[rd[1]].append((rd[0], rd[2]))
    
    distance = [maximum for _ in range(N+1)]
    distance[1] = 0
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for nnd in graph[node]:
            new_dist = distance[node] + nnd[1]
            if new_dist < distance[nnd[0]]:
                distance[nnd[0]] = new_dist
                queue.append(nnd[0])
            
    for d in distance:
        if d <= K:
            answer += 1
    return answer