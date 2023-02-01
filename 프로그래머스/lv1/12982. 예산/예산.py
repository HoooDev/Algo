def solution(d, budget):
    answer = 0
    d.sort()
    
    i = 0
    if sum(d) <= budget:
        answer = len(d)
    else:
        
        while budget > 0:
            if budget - d[i] < 0:
                break
            budget -= d[i]
            i+=1
            answer+=1
    
    return answer