class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid :
            return -1

        visit=set()
        minute= 0 
        rows,cols = len(grid), len(grid[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r,c) not in visit:
                    q.append((r,c))
                    visit.add((r,c))



        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        while q:
            isFresh=0
            for _ in range(len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr,nc) not in visit:
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        isFresh= 1
                    
            minute = minute + isFresh
       







        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    return -1

        return minute


