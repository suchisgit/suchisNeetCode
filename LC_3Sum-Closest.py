class Solution:
    def closest_two(nums,target):
        #diff=100000
        ln=len(nums)
        ptr1=0
        ptr2=ln-1
        while(ptr1+1<ptr2):
            s=nums[ptr1]+nums[ptr2]
            if(s<target):
                ptr1+=1
            elif(s>target):
                ptr2-=1
            else:
                break
        return nums[ptr1],nums[ptr2]
                
                
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l=len(nums)
        nums.sort()
        diff=100000
        for i in range(l):
            new_target=target-nums[i]
            new_nums=nums[0:i]+nums[i+1:l]
            num1,num2=Solution.closest_two(new_nums,new_target)
            s=nums[i]+num1+num2
            if(abs(s-target)<diff):
                ans=s
                diff=abs(s-target)
        return ans