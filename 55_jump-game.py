class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return max(m:=max(i and m,i+nums[i])for i in range(len(nums))if i==0 or i<=m)>=len(nums)-1
