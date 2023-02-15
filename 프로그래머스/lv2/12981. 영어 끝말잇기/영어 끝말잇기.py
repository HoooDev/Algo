def solution(n, words):
    answer = []
    
    dic = {words[0] : 1}
    # print(n)
    for i in range(1, len(words)):
        
        if words[i][0] != words[i-1][-1]:
            return [i % n + 1, i // n + 1]
        else:
            if words[i] not in dic:
                dic[words[i]] = 1
            else:
                dic[words[i]] += 1
                return [i % n + 1, i // n + 1]
    
    # print(dic)
    
    return [0, 0]