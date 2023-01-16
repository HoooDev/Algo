def solution(brown, yellow):
    answer = []
    garo = brown // 2 + 1
    
    for i in range(garo, 0, -1):
        for j in range(1, garo+1):
            if (i * 2) + ((j - 2) * 2) == brown and j - 2 > 0:
                if (i-2) * (j-2) == yellow:
                    answer.append(i)
                    answer.append(j)
                    return answer
        
    return answer