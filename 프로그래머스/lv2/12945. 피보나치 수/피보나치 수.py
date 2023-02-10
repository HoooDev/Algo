def solution(n):
    answer = 0
    # 0 1 1 2 3 5 8 13 21 34 ...
    stack = [0, 1]
    
    for i in range(100001):
        stack.append(stack[-1] + stack[-2])
        if i == n:
            answer = stack[n] % 1234567
    
    return answer