from collections import deque

def loc_p(place):
    p_li = []
    for i in range(len(place)):
        for j in range(len(place[0])):
            if place[i][j] == "P":
                p_li.append((i, j))
    return p_li

def bfs(place, a, b):
    is_zero = False
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = []
    cnt = 0
    for x in range(len(place)):
        visited.append([False] * len(place[0]))
        
    queue = deque([(a, b, cnt)])
    while queue:
        x, y, cnt = queue.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= len(place) or ny >= len(place[0]):
                continue
                
            elif visited[nx][ny] or place[nx][ny] == "X":
                continue
                
            elif place[nx][ny] == "P":
                cnt += 1
                visited[nx][ny] = True
       
                if (abs(a-nx) + abs(b-ny)) <= 2 and cnt<=2:
                        is_zero = True
                return is_zero

            elif place[nx][ny] == "O":
                queue.append((nx, ny, cnt+1))
    return False


def solution(places):
    answer = []
    for place in places:
        p_li = loc_p(place)
        is_z = False
        for p in p_li:
            l, r = p[0], p[1]
            if bfs(place, l, r):
                is_z = True
        if is_z:
            answer.append(0)
        else:
            answer.append(1)
    return answer
