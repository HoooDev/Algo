def solution(s):
    answer = -1
    stack = []
    
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    if stack:
        answer = 0
    else:
        answer = 1

    return answer