from itertools import combinations

def solution(orders, course):
    answer = []
    sum_orders = "".join(orders)
    set_orders = list(set(sum_orders))
    set_orders.sort()
    len_orders = sorted(orders, key=len)
    
    for c in course:
        if c > len(len_orders[-1]):
            break
        dic = {}
        combis = list(combinations(set_orders, c))
        for comb in combis:
            cnt = 0
            for order in orders:
                if len(order) < len(comb):
                    continue
                if len(set(comb) - set(order)) == 0:
                    cnt+=1
            if cnt >= 2:
                key = "".join(comb)
                dic[key] = cnt

        if len(dic.values())!=0:
            max_cnt = max(dic.values())
        
            for k, v in dic.items():
                if v == max_cnt:
                    answer.append(k)
        answer.sort()
            
    return answer

# 13,14,15 시간 초과(85/100)