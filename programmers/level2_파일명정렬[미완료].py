def solution(files):
    li=[]
    for file in files:
        for i in range(len(file)):
            if file[i].isdecimal() == True:
                head = file[:i]
                first_num = i
                break
        for j in range(first_num, len(file)):
            if file[j].isdecimal() == False:
                num = file[first_num:j]
                tail = file[j:]
                break
        li.append([head, num, tail])
        li.sort(key=lambda x: int(x[1]))
        li.sort(key=lambda x: x[0].lower())


        answer = ["".join(i) for i in li]

    return answer

# 25/100