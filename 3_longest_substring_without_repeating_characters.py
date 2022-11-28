class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return (lambda s,D,V:max(((V.__setitem__(1,V[1]+1)if D.get(c,-1)<V[0]else V.__setitem__(1,i-D[c])or V.__setitem__(0,D[c]+1))or D.__setitem__(c,i)or V[1]for i,c in enumerate(s)),default=0))(s,{},[0,0])


#=======================
# Explanation

# Expanded. Each line corresponds to a line in the original solution below
# V = [start, curLen]
# No need for maxLen bc we're using max to combine the loops
(lambda s,D,V:<INNER_LAMBDA>)(s,{},[0,0])
    max((<INNER_FOR> for i,c in enumerate(s)),default=0)
        <IF> if D.get(c,-1)<V[0] else <ELSE>
            # if
            V.__setitem__(1,V[1]+1)
            # else
            V.__setitem__(1,i-D[c])
            V.__setitem__(0,D[c]+1)
        D.__setitem__(c,i)
        V[1]

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        D = dict() # keep track of character -> last seen index so far
        start = 0
        curLen = 0
        maxLen = 0
        for i, c in enumerate(s):
            if D.get(c, -1) < start:
                curLen += 1
            else:
                curLen = i - D[c]
                start = D[c] + 1
            D[c] = i
            maxLen = max(maxLen, curLen)
            # print(i, c, curLen, maxLen)
        return maxLen