class Solution:
    def rob(self, nums: List[int]) -> int:
        return any(nums.__setitem__(i,max(nums[i-1], nums[i]+(i>1 and nums[i-2])))for i in range(1, len(nums)))or nums[-1]
