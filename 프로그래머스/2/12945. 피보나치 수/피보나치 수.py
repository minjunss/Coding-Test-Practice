def solution(n):
    return fibonacci(n) % 1234567

def fibonacci(n):
    fib_list = [1, 1]
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    
    return fib_list.pop()