class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        return(D:=Counter([s:=0]))and sum(D.update([s:=((s+x)%k)])or D[s]-1 for x in nums)
