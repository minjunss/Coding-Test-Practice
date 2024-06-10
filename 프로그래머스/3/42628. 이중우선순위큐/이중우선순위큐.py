from collections import deque
def solution(operations):
    answer = [0,0]
    queue = deque()

    for operation in operations:
        a = operation.split(' ')
        if a[0] == "I":
            queue.append(int(a[1]))
        elif queue:
            if a[1] == "1":
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))

    if queue:
        answer = [max(queue), min(queue)]

    return answer