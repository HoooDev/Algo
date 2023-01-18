def solution(price, money, count):
    answer = -1
    pay = 0
    for i in range(1, count + 1):
        pay += price * i
    if pay - money > 0:
        answer = pay - money
    else:
        answer = 0
    return answer