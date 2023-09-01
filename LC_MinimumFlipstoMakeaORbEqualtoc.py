class Solution:
    def bitsInNum(n):
        l=0
        while n>0:
            n=n>>1
            l+=1
        return l
    def minFlips(self, a: int, b: int, c: int) -> int:
        bitsA = Solution.bitsInNum(a)
        bitsB = Solution.bitsInNum(b)
        bitsC = Solution.bitsInNum(c)
        m = max(bitsA,bitsB,bitsC)
        op=0
        for i in range(m):
            if c&1==1:
                if a&1 == 0 and b&1 == 0:
                    op+=1
            else:
                if a&1 ==1 and b&1 ==1:
                    op+=2
                elif a&1 == 0 and b&1 == 0:
                    op+=0
                else:
                    op+=1
            a=a>>1
            b=b>>1
            c=c>>1
        return op
