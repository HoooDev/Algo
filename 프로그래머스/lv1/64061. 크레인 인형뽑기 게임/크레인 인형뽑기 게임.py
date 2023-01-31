def solution(board, moves):
    answer = 0
    N = len(board)
    pop_lst = []
    for i in moves:
        for j in range(N):
            if board[j][i-1] != 0:
                print('j:',j , 'i:', i-1)
                print(board[j][i-1], 'pop')
                if pop_lst:
                    if pop_lst[-1] == board[j][i-1]:
                        board[j][i-1] = 0
                        answer += 2
                        pop_lst.pop()
                    else:
                        pop_lst.append(board[j][i-1])
                        board[j][i-1] = 0
                        break
                else:
                    pop_lst.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
                # pop_lst.append(board[j][i-1])
                # board[j][i-1] = 0
                # if len(pop_lst) >= 1:
                #     if pop_lst[-1] == board[j][i-1]:
                #         pop_lst.pop()
                #         answer += 1
                break
        
            
    print(pop_lst)
    print(answer)
    return answer