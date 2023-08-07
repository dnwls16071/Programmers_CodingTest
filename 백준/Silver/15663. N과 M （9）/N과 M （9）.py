import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
li = list(map(int, input().strip().split()))
li.sort()
visited = [False] * N
res = []

def recursive():
    if len(res) == M:
        print(" ".join(map(str, res)))
        return
    else:
        flag = 0
        for i in range(len(li)):
            if not visited[i] and flag != li[i]:
                visited[i] = True
                res.append(li[i])
                flag = li[i]
                recursive()
                visited[i] = False
                res.pop()
recursive()