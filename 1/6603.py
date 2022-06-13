def pick(numbers, n, next_i):
    global lst
    if n == 6:
        print(*lst)
        return

    for i in range(next_i, len(numbers)):
        if visited[numbers[i]] == 0:
            lst.append(numbers[i])
            visited[numbers[i]] = 1
            pick(numbers, n+1, i)
            visited[numbers[i]] = 0
            lst.pop()

visited = [0] * 50
while True:
    lotto = list(map(int, input().split()))
    if lotto[0] == 0:
        break
    lst = []
    pick(lotto, 0, 1)
    print()

