def solution(s):
    n = len(s)
    s = list(s)
    global answer
    answer = 0
    
    def check(brackets):
        dic = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        global answer
        lst = []
        for i in brackets:
            if len(lst) == 0:
                lst.append(i)
            else:
                if i in dic.keys():
                    if dic[i] == lst[-1]:
                        lst.pop()
                else:
                    lst.append(i)
                    
        # print(lst, 'lst')
        if len(lst) == 0:
            answer += 1
                    
        return
        
    for i in range(n):
        a = s.pop(0)
        s.append(a)
        # print(s)
        check(s)

            
            
    return answer