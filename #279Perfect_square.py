import numpy as np

def findSquares(n,tot):
    a = []
    for i in range(1, int(np.sqrt(n)) + 1):
        a.append(i*i)

    if tot==1: return n

    if tot==2:
        for i in range(0,len(a)):
            for j in range(0,len(a)):
                if n==(a[i] + a[j]): return [a[i],a[j]]

    if tot==3:
        for i in range(0,len(a)):
            for j in range(0,len(a)):
                for k in range(0, len(a)):
                    if n==(a[i] + a[j] + a[k]): return [a[i],a[j],a[k]]

    if tot==4:
        for i in range(0, len(a)):
            for j in range(0, len(a)):
                for k in range(0, len(a)):
                    for g in range(0, len(a)):
                        if n==(a[i]+a[j]+a[k]+a[g]): return [a[i],a[j],a[k],a[g]]


def numSquares(n):
    f = [float('inf')] * (n + 1)
    for i in range(1, int(np.sqrt(n)) + 1):
        f[i * i] = 1
    for i in range(1, n + 1):
        for j in range(1, int(np.sqrt(n - i)) + 1):
            if f[i] + 1 < f[i + j * j]:
                f[i + j * j] = f[i] + 1


    return f[n]


n = 9999
ans = numSquares(n)
ans2 = findSquares(n,ans)
print(ans)
print(ans2)
print(np.sqrt(ans2))
