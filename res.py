def res(n):
     if n == 1:
             return 1
     else:
             for i in range(1,n+1):
                     res = 1
                     res = res * i
                     return res

res(1)
res(5)
