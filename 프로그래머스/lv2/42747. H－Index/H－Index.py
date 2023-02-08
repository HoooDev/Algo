def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    
    for i, j in enumerate(citations):
        if i >= j:
            return i
            
    return len(citations)