s = [[" "]*5 for _ in range(5)]
n =5
s[1][1]='a'
for i in range(n):
    for j in range(n):
        if s[i][j] != ' ':
            print(s[i][j], end='')
print()