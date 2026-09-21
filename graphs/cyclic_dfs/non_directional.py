graph = {
    'A': ['B','C'],
    'B': ['A','C'],
    'C': ['B', 'A']
}


def non_directional(nodes = graph) -> bool:
    visited = {node: False for node in graph}

    def dfs(n, parent):
        visited[n] = True


        for neighbour in graph[n]:
            if not visited[neighbour]:
                if dfs(neighbour, n):
                    return True
            elif neighbour != parent:
                print(f"{neighbour} are not equal {parent} hence cycle exist")
                return True

        visited[n] = True
        return False

    for n in nodes:
        if visited[n] == 0:
            if dfs(n, -1):
                return True

print (non_directional(graph))