def solution(numbers, target):
    answer = 0
    len_numbers = len(numbers)

    def dfs(numbers, target, idx):
        if idx < len_numbers:
            numbers[idx] *= 1
            dfs(numbers, target, idx+1)

            numbers[idx] *= -1
            dfs(numbers, target, idx+1)

        elif sum(numbers) == target:
            nonlocal answer
            answer += 1
            
    dfs(numbers, target, 0)
    return answer
