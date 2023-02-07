def solution(s):
    answer = ''
    lst = list(map(int, s.split(' ')))
    
    min_n = 1000000
    max_n = -100000
    
    a = min(lst)
    b = max(lst)
    
    answer = str(a) + " " + str(b)
    return answer