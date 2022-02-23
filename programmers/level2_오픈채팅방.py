def solution(record):
    logs = [r.split(' ') for r in record]
    user = {}
    for log in logs:
        if len(log)==3:
            user[log[1]] = log[2]
    res_li = []
    for log in logs:
        if log[0] == "Enter":
            res = f"{user[log[1]]}님이 들어왔습니다."
            res_li.append(res)

        elif log[0] == "Leave":
            res = f"{user[log[1]]}님이 나갔습니다."
            res_li.append(res)

    return res_li