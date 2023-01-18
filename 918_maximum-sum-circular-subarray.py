class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        return m if(s:=0)>(m:=max(s:=max(s+x,x)for x in nums))else(s:=0)+max(m,sum(nums)-min(s:=min(s+x,x)for x in nums))
