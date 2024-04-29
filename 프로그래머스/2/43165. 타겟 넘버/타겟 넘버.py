answer = 0
def solution(numbers, target):
    global answer
    dfs(numbers, 0, 0, target)
    return answer

def dfs(numbers, index, sum, target):
    global answer
    #탈출
    if index == len(numbers):
        if sum == target:
            answer += 1
        return;
    #재귀
    dfs(numbers, index + 1, sum + numbers[index], target)
    dfs(numbers, index + 1, sum - numbers[index], target)
