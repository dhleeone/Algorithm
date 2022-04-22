import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    cnt = 0
    for op in operations:
        s, n = op.split()
        if s == "I":
            heapq.heappush(max_heap, int(n)*(-1))
            heapq.heappush(min_heap, int(n))
            cnt += 1

        elif s == "D" and n == "1":
            if cnt == 0:
                continue
            else:
                heapq.heappop(max_heap)
                min_heap.pop()
                cnt-=1

        else:
            if cnt == 0:
                continue
            else:
                heapq.heappop(min_heap)
                max_heap.pop()
                cnt-=1
                
    if cnt == 0:
        return [0,0]
    else:
        max_val = heapq.heappop(max_heap)*(-1)
        min_val = heapq.heappop(min_heap)
        return [max_val, min_val]