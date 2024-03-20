import math

def solution(n, m):
    gcd = math.gcd(n,m)
    lcm = abs(n * m) // gcd
    answer = [gcd,lcm]
    return answer