from collections import deque

def matrix(place):
    mat = []
    for row in place:
        mat.append(list(row))
    return mat

def loc_p(mat):
    p_li = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "P":
                p_li.append((i, j))
    return p_li

def bfs(mat, a, b):
    is_zero = False
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = []
    cnt = 0
    for x in range(len(mat)):
        visited.append([False] * len(mat[0]))
        
    queue = deque([(a, b, cnt)])
    while queue:
        x, y, cnt = queue.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= len(mat) or ny >= len(mat[0]):
                continue
                
            elif visited[nx][ny] or mat[nx][ny] == "X":
                if cnt > 1:
                    cnt -= 1
                continue
                
            elif mat[nx][ny] == "P":
                cnt += 1

                visited[nx][ny] = True
                
                if (abs(a-nx) + abs(b-ny)) <= 2 and cnt<=2:
                        is_zero = True
                return is_zero

                
            elif mat[nx][ny] == "O":
                cnt += 1
                queue.append((nx, ny, cnt))

    return False


def solution(places):
    answer = []
    for place in places:
        mat = matrix(place)
        p_li = loc_p(mat)
        is_z = False
        for p in p_li:

            l, r = p[0], p[1]
            if bfs(mat, l, r):
                is_z = True
        if is_z:
            answer.append(0)
        else:
            answer.append(1)
        
    return answer

# 정확성
# 96.4 / 100.0
