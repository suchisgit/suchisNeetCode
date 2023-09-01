class Solution:
    def bsNegindx(ar):
        lo=0
        hi=len(ar)-1
        if ar[hi]>=0:
            return hi+1
        if ar[lo]<0:
            return lo
        while(lo<hi):
            m=lo+(hi-lo)//2
            if ar[m]>=0:
                lo=m+1
            else:
                hi=m
        return lo
    def countNegatives(self, grid: List[List[int]]) -> int:
        rightmostNegCol=len(grid[0])
        rows = len(grid)
        sol = 0
        for i,row in enumerate(grid):
            indx = Solution.bsNegindx(row)
            # print(indx)
            if indx < rightmostNegCol:
                # print(indx,rightmostNegCol)
                sol += (rows-i)*(rightmostNegCol-indx)
                # print(sol)
                rightmostNegCol=indx
        return sol
