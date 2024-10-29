def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)] # i = 인덱스, p = 우선 순위

    while queue:
        curr = queue.pop(0)

        if any(curr[1] < q[1] for q in queue):
            queue.append(curr)
        else:
            answer += 1
            if curr[0] == location:
                return answer

    return answer