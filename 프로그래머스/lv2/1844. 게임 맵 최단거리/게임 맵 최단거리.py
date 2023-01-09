from collections import deque

def solution(maps):

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))
    while q:
        cy, cx = q.popleft()
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if visited[ny][nx] == 0 and maps[ny][nx] == 1:
                    if ny == len(maps)-1 and nx == len(maps[0]) -1:
                        visited[ny][nx] += visited[cy][cx] + 1
                        print(visited)
                        return visited[ny][nx]
                    q.append((ny, nx))
                    visited[ny][nx] += visited[cy][cx] + 1

    return -1