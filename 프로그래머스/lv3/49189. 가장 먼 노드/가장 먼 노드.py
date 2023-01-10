from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    q = deque()

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    q.append(1)
    visited[1] = 1
    while q:
        n = q.popleft()
        for j in graph[n]:
            if visited[j] == 0:
                visited[j] = visited[n] + 1
                q.append(j)
            
    answer = visited.count(max(visited))
    return answer