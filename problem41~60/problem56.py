a, b = map(int, input().split())
print(((bool(a)and bool(not b)) or (bool(not a) and bool(b))))