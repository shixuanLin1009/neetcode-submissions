class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt_island = 0
        rows,cols = len(grid),len(grid[0])

        visit=set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q :
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r + dr ,c + dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visit.add((nr,nc))    
        for r in range(rows):
            for c in range(cols) :
                if grid[r][c] == "1" and(r,c) not in visit:
                    bfs(r,c)
                    cnt_island+=1

        return  cnt_island