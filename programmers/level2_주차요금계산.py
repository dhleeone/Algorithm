import math

def solution(fees, records):
    records.sort(key=lambda x:(x[6:10], x[0:5]))
    cars = list(set([i[6:10] for i in records]))
    cars.sort()
    dic = {}
    for i in cars:
        dic[i] = 0
            
    while records:
        rec1 = records.pop()
        rec1_time = int(rec1[:2])*60 + int(rec1[3:5])

        if rec1[11:] == "OUT":
            rec2 = records.pop()
            rec2_time = int(rec2[:2])*60 + int(rec2[3:5])
            gap = rec1_time - rec2_time
            
        elif rec1[11:] == "IN":
            default_time = 23*60 + 59
            gap = default_time - rec1_time
        dic[rec1[6:10]] += gap

    gap_li = list(dic.values())
    result_li = []
    
    for gap in gap_li:
        if gap<=fees[0]:
            result = fees[1]
        elif gap>fees[0]:
            gap -= fees[0]
            result = math.ceil(gap/fees[2])*fees[3] + fees[1]
        result_li.append(result)
        
    return result_li
