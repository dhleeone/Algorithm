from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    cnt_li = [0 for _ in range(n+1)]           
    queue = deque([1])
    visited = [1]
    while queue:
        node = queue.popleft()
        for nnd in graph[node]:
            if nnd not in visited:
                queue.append(nnd)
                visited.append(nnd)
                cnt_li[nnd] += (cnt_li[node] + 1)
    return cnt_li.count(max(cnt_li))


# 8, 9번 시간초과
