def solution(s):
    li = list(map(str, s))
    stack = []
    for i in range(len(li)):
        if len(stack)==0 or stack[-1] != li[i]:
            stack.append(li[i])
        elif len(stack)>0 and stack[-1] == li[i]:
            stack.pop()
    if stack==[]:
        return 1
    else:
        return 0