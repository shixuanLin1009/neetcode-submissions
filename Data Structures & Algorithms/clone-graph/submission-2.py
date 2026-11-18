"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # T O(V+E)
        if not node:
            return None
        o2n = {node:Node(node.val)}
        q = collections.deque([node])

        while q:
            cur = q.popleft()

            for neighbor in cur.neighbors:
                if neighbor not in o2n:
                    o2n[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                o2n[cur].neighbors.append(o2n[neighbor])
        
        return o2n[node]

#Output: [[2],[1,3],[2]]
#Input: adjList = [[2],[1,3],[2]]
# o2n = {nodeA(1):Node(node.val1)A_C}
# q = [nodeA(1)]
# while q[nodeA(1)] T
#   curA(1) = q.popleft()
#   for neighborB(2) in cur.neighbors[B(2)]:
#       if neighbor B(2) not in o2n{A(1):Node(node.val1)} T
#           o2n[neighborB(2)] = Node(neighborB(2).val2)B_C
#           q.append(neighborB(2))
#       o2n[curA(1)]A_C.neighbors.append(o2n[neighborB(2)]B_C)
# while q[B(2)] T
#   curB(2) = q.popleft()
#   for neighborA(1) in cur.neighbors[A(1),C(3)]:
#       if neighborA(1) not in o2n{A(1),B(2)} F
#       o2n[curB(2)]B_C.neighbors.append(o2n[neighborA(1)]A_C)
#   for neighborC(3) in cur.neighbors[A(1),C(3)]:
#       if neighborC(3) not in o2n{A(1),B(2)} T
#           o2n[neighborC(3)] = Node(neighbor.val3)C_C
#            q.append(neighborC(3))
#       o2n[curB(2)]B_C.neighbors.append(o2n[neighborC(3)]C_C)
# while q[C(3)] T
#   cur C(3) = q.popleft()
#   for neighborB(2) in cur.neighbors[B(2)]:
#       if neighborB(2) not in o2n{A(1),B(2),C(3)}F
#       o2n[curC(3)]C_C.neighbors.append(o2n[neighborB(2)]B_C)
# while q F
# return o2n[nodeA(1)]

