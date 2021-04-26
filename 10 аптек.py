s = []
ot = {}
ss = []
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if [a, b] not in ss:
        ss.append([a, b])
        s.append([a, b, i])
ss = []
s.sort()
h = 0
for i in range(len(s)):
    if s[i][0] > h:
        ot[s[i][2]] = [s[i][0], s[i][1]]
        h = s[i][1]
    elif s[i][1] > h:
        ot[s[i][2]] = [h + 1, s[i][1]]
        h = s[i][1]
    else:
        ot[s[i][2]] = [-1, -1]
for i in range(n):
    if i in ot:
        print(ot[i][0], ot[i][1])
    else:
        print(-1, -1)
