class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        return[C:=Counter(arr),arr.sort(key=abs)]and all(C[x]<1or C.subtract([x,x*2])or C[x*2]>=0for x in arr)
