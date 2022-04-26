def solution(skill, skill_trees):
    answer = 0
    li = []
    for st in skill_trees:
        val = ""
        for s in st:
            if s in skill:
                val += s
        is_skill = True
        for i in range(len(val)):
            if val[i] != skill[i]:
                is_skill = False
                break
        if is_skill:
            answer += 1            
    
    return answer