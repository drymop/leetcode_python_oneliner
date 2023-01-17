class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        return(t:=0)+min(min((t:=t+(s[i]>"0"))*2-i for i in range(len(s))),1)+len(s)-1-t
