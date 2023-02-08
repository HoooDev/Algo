from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    q = deque([[begin, 0]])
    
    while q:
        c_word, cnt = q.popleft()
        if c_word == target:
            return cnt
        
        for i in range(len(words)):
            check = 0
            word = words[i]
            for j in range(len(c_word)):
                if word[j] != c_word[j]:
                    check += 1
            if check == 1:
                q.append([word, cnt+1])
