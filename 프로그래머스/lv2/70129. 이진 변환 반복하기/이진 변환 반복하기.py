def solution(s):
    global answer
    answer = [0, 0]
    s = list(s)
    s = list(map(int, s))
    answer[1] = len(s) - sum(s) 
    print(sum(s))
    
    def binary(n):
        global answer
        arr = []
        while n >= 1:
            a = n % 2
            arr.append(a)
            n //= 2
        answer[1] += len(arr) - sum(arr)
        return arr
      
    while True:
        if len(s) == 1 and sum(s) == 1:
            return answer
        next_arr = binary(sum(s))
        answer[0] += 1
        # print(next_arr)
        s = list(map(int, next_arr))
        
    return answer