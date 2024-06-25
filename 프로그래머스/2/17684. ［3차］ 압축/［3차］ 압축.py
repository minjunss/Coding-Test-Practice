# w,c를 변수로 두는것에 집착하다보니 잘 안돼서 검색해서 참고함

def solution(msg):
    answer = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {letter: i + 1 for i, letter in enumerate(alphabet)}

    i = 0
    check = ''

    while i < len(msg):
        check += msg[i]
        if check in dic:
            i += 1
        else:
            dic[check] = len(dic) + 1
            answer.append(dic[check[:-1]])
            check = ''
    answer.append(dic[check])
    
    return answer
