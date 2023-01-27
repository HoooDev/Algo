

def solution(N, stages):
    answer = []
    ans_lst = []
    stages = sorted(stages)
    
    for stage in range(1, N+1):
        cnt = stages.count(stage)
        if len(stages) != 0:
            ans_lst.append([cnt/len(stages), stage])
            for i in range(cnt):
                stages.pop(0)
        else:
            ans_lst.append([0, stage])
            
        ans_lst.sort(key = lambda x : (-x[0], x[1]))
    # print(ans_lst)
                    
    for i in ans_lst:
        answer.append(i[1])
    return answer