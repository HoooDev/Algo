def solution(n):
    answer = 0
    stack = [0, 1]
    
    for i in range(n+1):
        stack.append(stack[-1] + stack[-2])
        if i == n:
            answer = stack[n] % 1234567
            # break
    
    return answer