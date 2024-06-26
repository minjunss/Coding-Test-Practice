import itertools
import collections


def solution(orders, course):
    answer = []
    
    for course_size in course:
        order_combination = []
        for order in orders:
            order_combination += itertools.combinations(sorted(order), course_size)
        most_order = collections.Counter(order_combination).most_common()

        answer += [''.join(key) for key, value in most_order if value == most_order[0][1] and value > 1]

    return sorted(answer)