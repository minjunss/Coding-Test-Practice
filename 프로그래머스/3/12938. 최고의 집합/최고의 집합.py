def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    quotient = s // n
    remainder = s % n
    
    answer = [quotient] * n
    
    for i in range(remainder):
        answer[n - 1 - i] += 1
    
    return answer