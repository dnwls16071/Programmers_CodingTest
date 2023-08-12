import sys
input = sys.stdin.readline

male_dict = {}
female_dict = {}
N, K = map(int, input().strip().split())
for _ in range(N):
    a, b  = map(int, input().strip().split())
    # b : 학년
    if b not in female_dict or b not in male_dict:
        # a : 성별
        if a == 1:  # 남학생
            male_dict[b] = 1
        else:
            female_dict[b] = 1
    else:
        if a == 1:  # 남학생
            male_dict[b] += 1
        else:
            female_dict[b] += 1

room = 0
for key, value in female_dict.items():
    if value % K == 0:
        room += value // K
    else:
        room += (value // K) + 1

for key, value in male_dict.items():
    if value % K == 0:
        room += value // K
    else:
        room += (value // K) + 1
print(room)