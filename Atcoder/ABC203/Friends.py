from operator import itemgetter
n, k = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

c = zip(a, b)
c = sorted(c)
a, b = zip(*c)

ans = k + sum(b)


print(a)
print(b)

for i in range(n):
    if i == 0:
        if k - a[0] < 0:
            ans = k
            break

    else:
        if k - a[i] + sum(b[:i-1]) < 0:
            ans = k + sum(b[:i-1])
            break


print(ans)
