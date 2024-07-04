#set으로 모든 종류 보석 개수 구하기
#딕셔너리로 현재구간 보석 종류와 개수 저장
#start end 0, 0
#end가 gems마지막까지 갈때까지 반복 end < len(gems)
#딕셔너리에 gems[end] + 1, end + 1
#딕셔너리 개수가 모든 종류 보석과 같으면
#end - start 랑 최소개수 비교, 최소개수 갱신
#딕셔너리에 gems[start] - 1, 0이면 딕셔너리에서 삭제
#start + 1

import collections

def solution(gems):
    answer = []
    gems_type_count = len(set(gems))
    current_gems_count = collections.defaultdict(int)
    start, end = 0, 0
    min = float('inf') #무한대
    
    while end < len(gems):
        current_gems_count[gems[end]] += 1
        end += 1
            
        while len(current_gems_count) == gems_type_count:
            if end - start < min:
                min = end - start
                answer = [start + 1, end]
            current_gems_count[gems[start]] -= 1
            if current_gems_count[gems[start]] == 0:
                current_gems_count.pop(gems[start])
            start += 1
    return answer