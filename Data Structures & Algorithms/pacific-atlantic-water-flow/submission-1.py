from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
       
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def bfs(starts, visit):
            q = deque(starts)
            visit.update(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit
                            and heights[nr][nc] >= heights[r][c]):
                        visit.add((nr, nc))
                        q.append((nr, nc))

        bfs([(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)], pac)
        bfs([(r, cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)], atl)
        return [[r, c] for r, c in pac & atl]