p1, p2, bit = map(int, input().split())
byte = p1 * p2 * bit / 8 / (1024 * 1024)
print("%.2f MB"%byte)