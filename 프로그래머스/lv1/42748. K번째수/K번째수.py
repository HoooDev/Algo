def solution(array, commands):
    answer = []
    
    for indexes in commands:
        copy_arr = array[::]
        i = indexes[0]
        j = indexes[1]
        k = indexes[2]
        a = copy_arr[i-1:j]
        a.sort()
        answer.append(a[k-1])
        
    return answer