from itertools import product

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    
#     answer = 10000000

#     for i in range(len(A)):
#         comp = 0
#         B.append(B.pop(0))
#         print(A, 'A')
#         print(B, 'B')
#         for j in range(len(B)):
#             comp += A[j] * B[j]
#         # A.append(A.pop(0))
            
#         print(comp)
#         if answer >= comp:
#             answer = comp
            
    

    return answer