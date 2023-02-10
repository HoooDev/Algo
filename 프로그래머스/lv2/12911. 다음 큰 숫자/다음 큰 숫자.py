def solution(n):
    
    
    def changeBinary(n):
        arr = []
        x = n
        while x >= 1:
            arr.append(x%2)
            x //= 2
        return arr
    
    n_cnt = changeBinary(n).count(1)
    
    for i in range(n+1, 1000001):
        if changeBinary(i).count(1) == n_cnt:
            return i
        
        
    
    answer = 0
    return answer