class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #move either down or to the right at any point in time.
        
        mem={}
        def f(m,n):
            if m == 0 :
                return f(0,n-1)
            elif n == 1:
                return 1

            if n== 0:
                return f(m-1,0)
            elif m==1:
                return 1
            if (m,n) in mem:return  mem[(m,n)]
            mem[(m,n)]= f(m-1,n) + f(m,n-1)

            return mem[(m,n)]

        return f(m,n)

# Input: m =2, n = 2

# Output: 2
# f(m2,n2)
#   if m == 0  F
#   if m == 1 and n== 0 F
#   f(m-1 1,n 2)
#       if m == 0 and n== 1 F
#       if m == 1 and n== 0 F
#       f(m1-1 0,n 2)
#           if m == 0 and n== 1 F
#   f(m-1,n)
#   mem[(m,n)]= f(m-1,n) + f(m,n-1)