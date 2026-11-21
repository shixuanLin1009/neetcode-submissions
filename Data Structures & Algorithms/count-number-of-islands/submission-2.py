class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        cnt = 0 
        rows, cols = len(grid), len(grid[0])
        
        visit = set()


        def bfs(r,c):
            if (r,c) in visit : return None

            q = collections.deque([(r,c)])
            visit.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + qr, dc +qc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visit.add((nr,nc))
            return None



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    cnt +=1
                    bfs(r,c)
                   
        
        return cnt

#name check :grid,cnt,rows,cols,visit,bfs,r,c,q,qc,qr
# ["1","0",
#  "0","1"]
# for 0 in range(rows):,for 0 in range(cols):
#   if grid[0][0] == "1"T
#       cnt +=1,cnt=1:
#       bfs(0,0)
#           if (0,0) in visit F:
#           q = collections.deque([(0,0)]),q=[(0,0)]
#           visit.add((0,0)),visit=((0,0))
#           directions = [[1,0],[-1,0],[0,1],[0,-1]]
#           while q T
#               0, 0 = q.popleft(),q=[]
#               for 1, 0 in directions:
#                   1, 0 = 0 + 1, 0 +0
#                   if  grid[1][0] == "1"F
#               for -1, 0 in directions:
#                   -1, 0 = 0 -1 1, 0 +0
#                   if 1 in range(rows) F
#               for 0, 1 in directions:
#                   0, 1 = 0 + 0, 0 + 1
#                   if grid[0][1] == "1" F
#               for 0, -1 in directions:
#                   0, -1 = 0 + 0, 0 + -1
#                   if -1 in range(cols) F
# for 0 in range(rows):,for 1 in range(cols):
# for 1 in range(rows):,for 0 in range(cols):
# if grid[0][0] == "1"T