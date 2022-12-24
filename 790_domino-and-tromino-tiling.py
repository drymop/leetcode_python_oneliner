class Solution:
    def numTilings(self, n: int) -> int:
        return (lambda Q:any(Q.append((Q[2]*2+Q.popleft())%1000000007)for _ in range(n))or Q[2])(deque((-1,0,1)))
