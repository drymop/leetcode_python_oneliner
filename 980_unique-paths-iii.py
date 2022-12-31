class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        return (lambda f:f(grid,*next((i,j)for i in range(len(grid))for j in range(len(grid[0]))if grid[i][j]==1),sum(x==0 for r in grid for x in r)+1,f))(lambda G,i,j,e,f:e==0 if G[i][j]==2 else(G[i].__setitem__(j,3),sum(f(G,x,y,e-1,f)for x,y in((i+1,j),(i,j+1),(i-1,j),(i,j-1))if 0<=x<len(G)and 0<=y<len(G[0])and 0<=G[x][y]<3),G[i].__setitem__(j,0))[1])
