from collections import deque

def solution(priorities, location):
    cnt = 0
    priorities[location] = str(priorities[location])
    queue = deque(priorities)
    
    while queue:
        val = queue.popleft()
        go_back = False
        
        for i in queue:
            if int(val) < int(i):
                go_back = True
                break
                
        if go_back == True:
            queue.append(val)
            
        else:
            cnt += 1
            if type(val) == str:
                return cnt