import sys
input = sys.stdin.readline

N = int(input())

num = 1
tot = 1
while True:
    if num ** 2 <= N < (num + 1) ** 2:
       print(tot)
       break
    num += 1
    tot += 1