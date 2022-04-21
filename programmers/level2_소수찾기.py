from itertools import permutations

def solution(numbers):
    answer = 0
    li = []
    for i in range(1, len(numbers)+1):
        per = list(permutations(numbers, i))
        for p in range(len(per)):
            per[p] = int("".join(per[p]))
            li.append(per[p])
    li = list(set(li))

    for num in li:
        cnt = 1
        if num == 0 or num == 1:
            continue
        for j in range(1, num//2+1):
            if num % j == 0:
                cnt += 1
        if cnt == 2:
            answer += 1
    return answer

