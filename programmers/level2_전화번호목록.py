def solution(pb):
    pb.sort()
    for i in range(len(pb)-1):
        idx = len(pb[i])
        if pb[i]==pb[i+1][:idx]:
            return False
    return True