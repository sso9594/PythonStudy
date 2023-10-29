a, b = map(int, input().split())
print((bool(not a) and bool(not b)) or (bool(a) and bool(b)))