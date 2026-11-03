class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        visited = {i:room for i, room in enumerate(rooms)}
    

        visiting = set()
        queue = [0]

        while queue:
             current_room = queue.pop(0)
             visiting.add(current_room)

             for key in visited[current_room]:
                       if key not in visiting:
                            queue.append(key)
    
        if len(visiting) == len(visited):
            return True
        else:
            return False
            

        # --- TIME COMPLEXITY ---   
        # O(N + E) depends on rooms and edges

        # --- SPACE COMPLEXITY ---  
        # 0(N) for queue as it depends on keys found of room
        # 0(N) for queue depends on rooms

          

        

        
        