def solution(dartResult):
    answer = 0
    cal_lst = []
    format_lst = dartResult.replace('10', 'X')
    print(format_lst)
    for i in format_lst:
        if i.isnumeric() == True :
            cal_lst.append(int(i))
        if i == 'X':
            cal_lst.append(10)
        if i == 'S':
            cal_lst[-1] **= 1
        if i == 'D':
            cal_lst[-1] **= 2
        if i == 'T':
            cal_lst[-1] **= 3
        if i == '*':
            if len(cal_lst) >= 2:
                cal_lst[-1] *= 2
                cal_lst[-2] *= 2
            else:
                cal_lst[-1] *= 2
        if i == '#':
            cal_lst[-1] = -cal_lst[-1]

    answer = sum(cal_lst)
    return answer