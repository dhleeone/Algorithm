def solution(s):
    if s[0] == ")" or s[-1]=="(":
        return False

    li = []
    for i in s:
        if i == "(":
            li.append("(")
        elif i == ")" and len(li) > 0:
            li.pop()        
    if li == []:
        return True
    else:
        return False