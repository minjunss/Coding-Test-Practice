# 딕셔너리에 종류, 옷 넣기
# 옷 종류 개수+1 곱하기 (안입어도 되니까)
# 결과 값에서 -1 (아무것도 안입으면 안되니까)

def solution(clothes):
    closet = {}
    
    for name, kind in clothes:
        if kind in closet.keys():
            closet[kind] += [name]
        else:
            closet[kind] = [name]
    
    answer = 1
    
    for key, value in closet.items():
        answer *= (len(value) + 1)
    
    return answer - 1