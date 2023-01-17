from itertools import permutations

def solution(k, dungeons):
    answer = -1
    max_cnt = 0
    per_dg = permutations(dungeons, len(dungeons))
    for i in per_dg:
        piro = k
        cnt = 0
        for j in i:
            if piro >= j[0] and piro-j[1] >= 0:
                piro -= j[1]
                cnt += 1
            else:
                break
        if answer < cnt:
            answer = cnt
                
    
    return answer