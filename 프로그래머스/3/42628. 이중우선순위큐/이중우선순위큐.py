import heapq

def solution(operations):
    answer = [0, 0]
    min_heap = []
    max_heap = []
    entry_count = {}

    for operation in operations:
        if operation.startswith("I "):
            num = int(operation.split()[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in entry_count:
                entry_count[num] += 1
            else:
                entry_count[num] = 1
        elif operation == "D 1":
            while max_heap and entry_count[-max_heap[0]] == 0:
                heapq.heappop(max_heap)
            if max_heap:
                max_value = -heapq.heappop(max_heap)
                entry_count[max_value] -= 1
        elif operation == "D -1":
            while min_heap and entry_count[min_heap[0]] == 0:
                heapq.heappop(min_heap)
            if min_heap:
                min_value = heapq.heappop(min_heap)
                entry_count[min_value] -= 1

    while min_heap and entry_count[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_count[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        answer = [-max_heap[0], min_heap[0]]

    return answer
