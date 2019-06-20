from collections import defaultdict

n, m = map(int, input().split(' '))


input1 = list()
for i in range(n):
    input1.append(input())

    input2 = list()
for i in range(m):
    input2.append(input())

d = defaultdict(list)

for i in range(n):
    d[input1[i]].append(i + 1)

for i in input2:
    if i in d:
        print(*d[i])
    else:
        print(-1)
