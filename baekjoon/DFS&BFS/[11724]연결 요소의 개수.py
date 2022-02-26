import sys
sys.setrecursionlimit(10000)

read = sys.stdin.readline
n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(start, graph, visited):
        visited[start] = 1
        for i in graph[start]:
            if visited[i] == 0:
                dfs(i , graph, visited)
                
visited = [0]*(n+1)
cnt = 0

for j in range(1, n+1):
    if visited[j] == 0:
        dfs(j , graph, visited)
        cnt+=1
    else:
        continue
        
print(cnt)