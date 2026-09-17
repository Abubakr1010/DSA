# There is a bi-directional graph with n vertices, 
# where each vertex is labeled from 0 to n - 1 (inclusive). 
# The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists 
# from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, 
# return true if there is a valid path from source to destination, 
# or false otherwise.
from typing import List
from collections import deque




class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

 
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        queue = deque([source])
        visited = {source}

        while queue:
            curr = queue.popleft()

            if curr == destination:
                return True
            
            for nbr in graph[curr]:
                if nbr == destination:
                    return True
                if nbr not in visited:
                    visited.add(nbr)
                queue.append(nbr)

            return False

        # --- TIME COMPLEXITY ---
        # O(V+E) it depends on vertex and edges connected to
        # --- SPACE COMPLEXITY ---
        # O(V+E) becaouse of adjececent list is created
        # O(V) for visited and creating queue




    