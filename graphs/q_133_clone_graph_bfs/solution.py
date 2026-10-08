from typing import Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []




class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        
        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbour in curr.neighbors:
                if neighbour not in clones:
                    clones[neighbour] = Node(neighbour.val)
                    queue.append(neighbour)

                clones[curr].neighbors.append(clones[neighbour])
        return clones[node]

    # --- TIME COMPLEXITY ---
    # O(N + N) to add nodes and it neighbour

    # --- SPACE COMPLEXITY ---
    # O(N + N) number of nodes and list of neighbours
        






