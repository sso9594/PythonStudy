a, m, d, n = map(int, input().split())
target = a
for i in range(1,n):
    target = target * m + d
print(target)