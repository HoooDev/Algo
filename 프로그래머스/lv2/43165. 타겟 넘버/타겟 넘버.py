def solution(numbers, target):
    answer = 0
    ans_lst = [0]
    for i in numbers:
        sum_minus_lst = []
        for j in ans_lst:
            sum_minus_lst.append(j+i)
            sum_minus_lst.append(j-i)
        ans_lst = sum_minus_lst
    answer = ans_lst.count(target)
    return answer