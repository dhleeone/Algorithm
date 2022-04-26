def solution(dirs):
    li = [(0,0)]
    set_li = []
    
    for di in dirs:
        x = li[-1][0]
        y = li[-1][1]
        if di == "U" and y < 5:
            nx = x
            ny = y+1
            li.append((nx, ny))
            set_li.append((x+nx, y+ny))
            
        elif di == "D" and y > -5:
            nx = x
            ny = y-1
            li.append((nx, ny))
            set_li.append((x+nx, y+ny))
            
        elif di == "L" and x > -5:
            nx = x-1
            ny = y
            li.append((nx, ny))
            set_li.append((x+nx, y+ny))
        
        elif di == "R" and x < 5:
            nx = x+1
            ny = y
            li.append((nx, ny))     
            set_li.append((x+nx, y+ny))

    answer = len(set(set_li))
    return answer