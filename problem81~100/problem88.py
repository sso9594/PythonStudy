a, d, n = map(int, input().split())
target = a
for i in range(1, n):
    target += d
print(target)