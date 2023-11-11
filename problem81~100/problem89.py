a, r, n = map(int, input().split())
target = a
for i in range(1,n):
    target*=r
print(target)