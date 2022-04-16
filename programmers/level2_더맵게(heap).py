import heapq

def solution(scov, K):
    heapq.heapify(scov)
    max_loop = len(scov)-1
    cnt = 0
    while scov[0] < K:
        if len(scov) == 1:
            return -1
        
        if cnt == max_loop:
            return -1
        
        least = heapq.heappop(scov) 
        second = heapq.heappop(scov) 
        new = least + (second*2)
        heapq.heappush(scov, new)
        cnt += 1

    return cnt