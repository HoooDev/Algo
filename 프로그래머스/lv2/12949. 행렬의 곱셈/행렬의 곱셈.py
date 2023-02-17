def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        num_sum_lst = []
        for j in range(len(arr2[0])):
            num_lst = []
            for k in range(len(arr1[i])):

                num_lst.append(arr1[i][k] * arr2[k][j])
            num_sum_lst.append(sum(num_lst))
        answer.append(num_sum_lst)

        
    # for i in range(len(arr1)):
    #     num_sum_lst = []
    #     for j in range(len(arr2)):
    #         num_lst = []
    #         for k in range(len(arr2[j])):
    #             num_lst.append(arr1[i][k] * arr2[k][j])
    #         num_sum_lst.append(sum(num_lst))
    #     answer.append(num_sum_lst)
        
    return answer