def solution(s):
    s=s[1:-1]
    li = []
    for i in range(len(s)):
        if s[i] == "{":
            start = i+1
        elif s[i] == "}":
            end = i
            val = s[start:end]
            res = list(map(int, val.split(",")))
            li.append(res)
    li.sort(key=len)
    answer = []
    for i in li:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer