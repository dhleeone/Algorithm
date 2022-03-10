from itertools import permutations

def solution(expression):
    ops = ['+', '-', '*']
    ops = list(permutations(ops))
    
    exp = []
    num = ""
    for i in range(len(expression)):
        if expression[i].isdigit():
            num += expression[i]

        elif not expression[i].isdigit():
            exp.append(int(num))
            exp.append(expression[i])
            num = ""
        if i == len(expression) - 1:
            exp.append(int(num))
            
    answer_li = []
    for op in ops:
        exp_c = exp.copy()
        for idx in range(3):
            cnt = exp_c.count(op[idx])
            for _ in range(cnt):
                for i in range(1, len(exp_c)-1):
                    if exp_c[i] == op[idx]:
                        if op[idx] == "-":
                            minus = exp_c[i-1] - exp_c[i+1]
                            exp_c[i-1] = minus
                            del exp_c[i:i+2]

                        elif op[idx] == "+":
                            plus = exp_c[i-1] + exp_c[i+1]
                            exp_c[i-1] = plus
                            del exp_c[i:i+2]
                            
                        elif op[idx] == "*":
                            mul = exp_c[i-1] * exp_c[i+1]
                            exp_c[i-1] = mul
                            del exp_c[i:i+2]                        
                        break
        answer_li.append(abs(exp_c[0]))
    answer = max(answer_li)
    
    return answer
