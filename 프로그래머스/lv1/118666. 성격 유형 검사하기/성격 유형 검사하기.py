def solution(survey, choices):
    answer = ''
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    mbti = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    mbti_lst=['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    for i in range(len(survey)):
        if choices[i] < 4:
            mbti[survey[i][0]] += score[choices[i]]
        elif choices[i] > 4:
            mbti[survey[i][1]] += score[choices[i]]

    for i in range(0, len(mbti_lst), 2):
        if mbti[mbti_lst[i]] > mbti[mbti_lst[i+1]]:
            lst = [mbti_lst[i], mbti_lst[i+1]]
            answer += mbti_lst[i]
        elif mbti[mbti_lst[i]] < mbti[mbti_lst[i+1]]:
            answer += mbti_lst[i+1]
        elif mbti[mbti_lst[i]] == mbti[mbti_lst[i+1]]:
            lst = [mbti_lst[i], mbti_lst[i+1]]
            lst.sort()
            answer += lst[0]
            
    return answer