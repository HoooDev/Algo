from itertools import combinations

def solution(nums):
    global answer
    answer = 0

    
    def is_prime(num):
        global answer

        cnt = 0
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                cnt += 1

        if cnt == 1:
            answer += 1
            return
        
    prime_lst = list(combinations(nums, 3))
    
    for i in prime_lst:
        is_prime(sum(i))
        
    return answer