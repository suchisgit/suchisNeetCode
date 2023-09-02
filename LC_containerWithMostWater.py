class Solution:
    def maxArea(self, height: List[int]) -> int:
        MaxArea=0
        l=len(height)
        p1=0
        p2=l-1
        while(p1<p2):
            if(height[p1]<height[p2]):
                area=height[p1]*(p2-p1)
                if(area>MaxArea):
                    MaxArea=area
                p1+=1
            else:
                area=height[p2]*(p2-p1)
                if(area>MaxArea):
                    MaxArea=area
                p2-=1
        return MaxArea