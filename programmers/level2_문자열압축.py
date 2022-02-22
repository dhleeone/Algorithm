def solution(s):
    
    li = [len(s)]

    for seq in range(1, len(s)//2+1):

        res = ""
        cnt = 1
        next_idx = 0

        for idx in range(len(s)):

            if idx < next_idx:
                continue;

            # 연속될 때 처리
            if s[idx:idx+seq] == s[idx+seq:idx+2*seq]:
                cnt+=1
                next_idx = idx+seq

            # 연속되다가 달라질 때
            elif cnt>1 and (s[idx:idx+seq] != s[idx+seq:idx+2*seq]):
                val = str(cnt) + s[idx:idx+seq]
                res += val
                cnt = 1
                next_idx = idx+seq

            # 처음부터 다를 때 
            elif cnt == 1 and (s[idx:idx+seq] != s[idx+seq:idx+2*seq]):
                val_2 = s[idx:idx+seq]
                res += val_2
                next_idx = idx+seq

        if res!="":
            li.append(len(res))
            
    answer = min(li)
    return answer