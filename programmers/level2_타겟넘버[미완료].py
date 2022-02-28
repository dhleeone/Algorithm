def solution(numbers, target):
    stack = []
    
    def dfs(numbers, target, start):
        nonlocal stack    
        if start>len(numbers)-1:
            return 

        numbers[start] = (-1) * numbers[start]
        
        if sum(numbers) == target:
            if numbers not in stack:
                stack.append(numbers)
                return

        elif sum(numbers)>target:
            dfs(numbers, target, start+1)

        elif sum(numbers)<target:
            numbers[start] = (-1) * numbers[start]
            dfs(numbers, target, start+1)
    
    if sum(numbers) == target:
        return 1

    for i in range(len(numbers)):
        reset_numbers = numbers.copy()
        dfs(reset_numbers, target, i)
        answer=len(stack)
        
    return answer
