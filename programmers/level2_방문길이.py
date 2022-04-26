def solution(dirs):
    li = [(0,0)]
    set_li = []
    
    for di in dirs:
        x, y = li[-1][0], li[-1][1]
        if di == "U" and y < 5:
            nx, ny = x, y+1
            li.append((nx, ny))
            set_li.append((x+nx, y+ny))
            
        elif di == "D" and y > -5:
            nx, ny = x, y-1
            li.append((nx, ny))
            set_li.append((x+nx, y+ny))
            
        elif di == "L" and x > -5:
            nx, ny = x-1, y
            li.append((nx, ny))
            set_li.append((x+nx, y+ny))
        
        elif di == "R" and x < 5:
            nx, ny = x+1, y
            li.append((nx, ny))     
            set_li.append((x+nx, y+ny))
            
    answer = len(set(set_li))
    return answer
