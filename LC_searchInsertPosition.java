class Solution {
    
    public int searchInsert(int[] nums, int target) {
        int lo=0;
        int hi=nums.length-1;
        if(nums[hi]<target){
            return hi+1;
        }
        while(lo<hi){
            int m=lo+(hi-lo)/2;
            if(nums[m]<target){
                lo=m+1;
            }
            else{
                hi=m;
            }
        }
        return lo;    
    }
}