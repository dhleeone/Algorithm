# 1차 - 미통과
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


# 2차 - 해결
def solution(files):
    li=[]
    for file in files:
        num_fin = False
        head, num, tail = '', '', ''
        for i in range(len(file)):
            if not num_fin and file[i].isdigit()==False:
                head += file[i]
            elif file[i].isdigit():
                num_fin = True
                num +=file[i]
            else:
                tail+=file[i:]
                break
        li.append((head, num, tail))
        
    li.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = ["".join(i) for i in li]

    return answer

#for문 줄이기, 런타임에러 해소
