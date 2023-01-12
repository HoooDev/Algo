from collections import deque

def solution(n, wires):
    answer = -1
    min = 10000000000
    for i in range(n-1):
        global visited
        wires2 = wires[::]
        graph = [[] for _ in range(n+1)]
        wires2.pop(i)
        visited = [0] * (n+1)
        
        for j in wires2:
            graph[j[0]].append(j[1])
            graph[j[1]].append(j[0])
        # print(graph)
        
        def dfs(i):
            global visited
            global cnt
            visited[i] = 1
            for j in graph[i]:
                if visited[j] == 0:
                    visited[j] = 1
                    cnt += 1
                    dfs(j)
            return cnt
        
        ans = []
        cal = []
        for x in range(1, n+1):
            global cnt
            cnt = 0
            if visited[x] == 0:
                # print(x, 'x')
                # print(dfs(x))
                # print(visited)
                cal.append(dfs(x))
        #         print('----------')
        # print(cal, 'cal')
        # print(abs(cal[0] - cal[1]), 'calcal')
        if min > abs(cal[0] - cal[1]):
            min = abs(cal[0] - cal[1])

        # result.append()
    return min