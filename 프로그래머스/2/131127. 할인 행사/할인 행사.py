from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    item = {w:n for w,n in zip(want,number)}
    
    for i in range(len(discount)):
        if item == Counter(discount[i:i+10]):
            answer += 1
    
    return answer