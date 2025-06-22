a, b, c, d, e, f = map(int,input().split())

den = a*e - b*d
x = int((c*e - b*f) / den)
y = int((a*f - c*d) / den)
print(x, y)