"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visit= {node:Node(node.val)}

        q = collections.deque([node]) #deque needs an iterable,
    
        while q :
            cur_node = q.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in visit:
                    visit[neighbor]=Node(neighbor.val)
                    q.append(neighbor)
                visit[cur_node].neighbors.append(visit[neighbor])   

        return visit[node]
            