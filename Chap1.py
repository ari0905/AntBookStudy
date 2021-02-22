#Chap 1-6
#p21
"""
n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            length = a[i] + a[j] + a[k]
            ma = max(a[i], max(a[j], a[k]))
            rest = length - ma
            if rest > ma:
                ans = max(ans, length)
print(ans)
"""
#p23

L = int(input())
n = int(input())
x = list(map(int, input().split()))

minT, maxT = 0, 0

for i in range(n):
    minT = max(minT, min(x[i], L - x[i]))
    maxT = max(maxT, max(x[i], L - x[i]))

print("min = {}".format(minT))
print("max = {}".format(maxT))