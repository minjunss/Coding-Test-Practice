def solution(k, d):
    count = 0

    # for a in range(0, d + 1, k):
    #     for b in range(0, d + 1, k):
    #         if a * a + b * b <= d * d:
    #             count += 1
    
    for x in range(0, d + 1, k):
        max_y = (d**2 - x**2) ** 0.5
        count += (max_y//k) + 1
        
    return count
