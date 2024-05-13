# 스택에 괄호 여는거 쌓고
# 닫힌 괄호랑 스택 팝이랑 다른 종류면 false
# 다 끝나고 스택에 남아있으면 false


def solution(s):
    answer = 0
    
    for i in range(len(s)):
        a = s[i:] + s[:i]
        if bracket_check(a):
            answer += 1
    return answer

def bracket_check(s):
    stack = []
    bracket = {')':'(', '}':'{', ']':'['}
    
    for char in s:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket.keys():
            if not stack or stack.pop() != bracket[char]:
                return False
            
    return len(stack) == 0
            
            
            
    
    
    
    