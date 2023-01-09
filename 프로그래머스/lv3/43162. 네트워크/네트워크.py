def solution(n, computers):
    global arr
    answer = 0
    arr = [[] for _ in range(n)]
    visited = [0] * n
    # print(arr)
    # print(visited)
    for i in range(n):
            for j in range(n):
                if computers[i][j] != 0 and i != j:
                    arr[i].append(j)
                    
    def dfs(a):
        global arr
        for i in arr[a]:
            if visited[i] == 0:
                visited[i] = 1
                dfs(i)

    for q in range(n):
        if visited[q] == 0:
            dfs(q)
            answer += 1
    
#     print(visited, 'visi')
    
#     print(arr, 'arr')
            
    return answer