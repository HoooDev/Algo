def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    lower_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    is_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(new_id)):
        if new_id[i] in lower_alpha or new_id[i] in is_num or new_id[i]== '-' or new_id[i]=='.' or new_id[i] == '_':
            answer += new_id[i]

    for i in range(len(answer)+1, 0, -1 ):
        answer = answer.replace('.'*i, '.')
        
    # print(answer)
    
    if len(answer) != 0:
        id_lst = list(answer)
        if id_lst[0] == '.':
            id_lst[0] = ''
        if id_lst[-1] == '.':
            id_lst[-1] = ''
        answer = ''.join(id_lst)
    if len(answer) == 0:
        answer += 'a'
        
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[0:len(answer)-1]
    
    if len(answer) <= 2:
        print(answer, '22123123')
        while len(answer) < 3:
            answer += answer[-1]
    
    # print(answer)
    return answer