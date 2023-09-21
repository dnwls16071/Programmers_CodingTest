from collections import deque
import sys
input = sys.stdin.readline

q = deque()
N = int(input())
for _ in range(N):
    command = list(map(int, input().strip().split()))
    # 1 X : 정수 X를 덱의 앞에 넣는다.
    # 2 X: 정수 X를 덱의 뒤에 넣는다.
    if len(command) == 2:
        if command[0] == 1:
            q.appendleft(command[1])
        elif command[0] == 2:
            q.append(command[1])
    elif len(command) == 1:
        # 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        if command[0] == 3:
            if len(q) == 0:
                print(-1)
            else:
                temp = q.popleft()
                print(temp)
        # 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        elif command[0] == 4:
            if len(q) == 0:
                print(-1)
            else:
                temp = q.pop()
                print(temp)
        # 5: 덱에 들어있는 정수의 개수를 출력한다.
        elif command[0] == 5:
            print(len(q))
        # 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
        elif command[0] == 6:
            if len(q) == 0:
                print(1)
            else:
                print(0)
        # 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        elif command[0] == 7:
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        # 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        elif command[0] == 8:
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])