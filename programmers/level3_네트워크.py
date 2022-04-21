def solution(n, computers):
    graph = [[] for _ in range(n)] 
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            elif computers[i][j] == 1:
                graph[i].append(j)
    
    visited = []
    cnt = 0
    for x in range(n):
        if x in visited:
            continue
        stack = [x]
        while stack:
            node = stack.pop()
            visited.append(node)
            for nnd in graph[node]:
                if nnd not in visited:
                    stack.append(nnd)
        cnt+=1
    return cnt