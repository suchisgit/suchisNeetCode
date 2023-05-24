class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<tuple<int,int>> numIndx;
        for(int i=0;i<nums.size();i++){
            numIndx.push_back( make_tuple(nums[i],i) );
        }
        sort(numIndx.begin(),numIndx.end());
        int l = 0 ;
        int r = nums.size()-1;
        vector<int> res;
        while(l<r){
            if( get<0>(numIndx[l])+ get<0>(numIndx[r]) > target ){
                r--;
            }else if ( get<0>(numIndx[l])+ get<0>(numIndx[r]) < target){
                l++;
            }else{
                res = {get<1>(numIndx[l]),get<1>(numIndx[r])};
                break;
            }
        }
        return res;
    }
};