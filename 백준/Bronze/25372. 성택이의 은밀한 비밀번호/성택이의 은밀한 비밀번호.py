N = int(input())
for _ in range(N):
    String = input().strip()
    if 6 <= len(String) <= 9:
        print("yes")
    else:
        print("no")