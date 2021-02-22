#Chap 1-6
#p21
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
