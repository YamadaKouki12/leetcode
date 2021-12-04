class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        map<int,int> ma;
        for(int i=0; i<n; i++){
            ma[nums[i]] = i;
        }
        for(int i=0; i<n; i++){
            if(nums[i]+nums[ma[nums[i]]]==target && i!=ma[nums[i]]){
                return {i, ma[nums[i]]};
            }
        }
        return {};
    }
};