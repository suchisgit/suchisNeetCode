//1 , 3, 5, 8, 9, 10
class Solution {
    public int binarySearch(int[] arr,int target){
        int lo=0;
        int hi=arr.length-1;
        while(hi>lo){
            int m=lo+(hi-lo)/2;
            if (arr[m]<target){
                lo=m+1;
            }else{
                hi=m;
            }
        }
        return lo;
    }
    public int[] searchRange(int[] nums, int target) {
        int[] res={-1,-1};
        int ser2;
        if (nums.length==0){
            return res;
        }
        
        int ser1=binarySearch(nums,target);
        if (nums[ser1]!=target){
            return res;
        }
        if (target==nums[nums.length-1]){
            ser2=nums.length;
        }else{
            ser2=binarySearch(nums,target+1);
        }
        res[0]=ser1;
        res[1]=ser2-1;
        return res;
    }
}