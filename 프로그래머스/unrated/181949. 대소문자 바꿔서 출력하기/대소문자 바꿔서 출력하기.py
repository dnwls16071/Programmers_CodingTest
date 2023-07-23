str = input()
answer = ''

for i in str:
    if i.islower():
        answer += i.upper()
    else:
        answer += i.lower()
print(answer)
    
