def solution(n):
    cnt = 0
    for start in range(1, n+1):
        val = 0
        for num in range(start,n+2):
            val += num
            if val == n:
                cnt += 1
                break
            elif val > n:
                break

    return cnt