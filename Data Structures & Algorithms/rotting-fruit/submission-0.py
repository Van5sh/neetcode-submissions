class Solution:
    '''
        [1,1,0]
        [0,1,1]
        [0,1,2]
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dire=[(1,0),(0,1),(-1,0),(0,-1)]
        fresh=0
        time=0
        rot=0
        q=deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        while fresh>0 and q:
            length=len(q)
            for i in range(length):
                r,c=q.popleft()
                for dx,dy in dire:
                    row,col=r+dx,c+dy
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1):
                        grid[row][col]=2
                        q.append((row,col))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
        