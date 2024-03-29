# 스택이랑 numbers길이만큼의 -1로 채워진 리스트 초기화

# numbers를 뒤에서부터 순회
# 스택에 값이 있고 스택의 젤 윗값이 numbers 현재값보다 작다면 while 스택 pop
# 스택에 값이 있으면 -1로 채워진 리스트의 현재 인덱스를 스택의 제일 윗 값을 적용
# 스택에 numbers의 현재값 쌓기

def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    
    for i in range(len(numbers)-1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(numbers[i])
        
    return answer