from collections import deque

def solution(k, room_number):
    answer = []
    left_room = [True for i in range(k+1)]
    left_room[0] = False
    
    
    queue = deque(room_number)
    while queue:
        rn = queue.popleft()
        
        if left_room[rn]:
            answer.append(rn)
            left_room[rn] = False
            
        else:
            next_num = rn + 1
            
            for idx in range(next_num, k+1):
                if left_room[idx] == True:
                    answer.append(idx)
                    left_room[idx] = False
                    break

    return answer

# 효율성 미통과