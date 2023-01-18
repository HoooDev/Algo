def solution(X, Y):
    answer = ''
    count_X = [0] * 10
    count_Y = [0] * 10
    
    for i in [X, Y]:
        for j in i:
            if i == X:
                count_X[int(j)] += 1
            else:
                count_Y[int(j)] += 1

    for i in range(9, -1, -1):
        add = ''

        if count_X[i] <= count_Y[i]:
            add = str(i)*count_X[i]
        else:
            add = str(i)*count_Y[i]
        answer += add
        
    if answer == '':
        answer = '-1'
    if answer[0] == '0':
        answer = '0'
    
    return answer