def solution(n, arr1, arr2):
    answer = []

    result = []
    for arr in [arr1, arr2]:
        map = []
        for i in range(n):
            get_map = []
            m = arr[i]
            while m >= 1:
                a = m % 2
                get_map.append(a)
                m //= 2
            if len(get_map) < n:
                while len(get_map) < n:
                    get_map.append(0)
            map.append(get_map[::-1])
        result.append(map)
        
    for i in range(n):
        map_str = ''
        for j in range(n):
            if result[0][i][j] == 0 and result[1][i][j] == 0:
                map_str += ' '
            else:
                map_str += '#'
        answer.append(map_str)
    # print(answer)
    return answer