s = []
ot = {}
for i in range(int(input())):
    a, b = map(int, input().split())
    s.append([a, b, i])
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
for key in sorted(ot.keys()):
    print(*ot[key])

