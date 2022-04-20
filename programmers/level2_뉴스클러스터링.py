def preprocess(string):
    li = []
    for i in range(len(string)-1):
        sep = string[i:i+2]
        if sep.isalpha() and len(sep)==2:
            li.append(sep.lower())
    return li

def unionprocess(string, inner):
    li = []
    for s in string:
        if s not in inner:
            li.append(s)
    return li

def solution(str1, str2):
    str_1, str_2 = preprocess(str1), preprocess(str2)
    inner = list(set(str_1)&set(str_2))
    outer = len(unionprocess(str_1, inner)+unionprocess(str_2, inner))
    min_num, max_num = 0
    
    for i in inner:
        a = str_1.count(i)
        b = str_2.count(i)
        min_num += min(a, b)
        max_num += max(a, b)
    outer += max_num
    if outer == 0:
        return 65536
    sim = min_num / outer
    answer = int((min_num / outer) * 65536)
    return answer
    