def solution(numbers):
    answer = -1
    for i in range(10):
        if i not in numbers:
            answer += i
    answer += 1
    return answer