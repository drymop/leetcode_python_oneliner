class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        return next((i for i, r in enumerate(sorted(c-r for c,r in zip(capacity,rocks)))if(additionalRocks:=additionalRocks-r)<0),len(rocks))
