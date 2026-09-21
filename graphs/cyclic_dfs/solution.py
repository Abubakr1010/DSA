
graph = {
    0:[1],
    1:[2],
    2:[0]
}

# cyclic graph

def cyclic_graph( num_of_nodes:int, graph = graph) -> bool:
    visited = [0] * num_of_nodes

    def dfs(node):
        visited[node] = 1

        for neighbour in graph[node]:
            if visited[neighbour] == 1:
                print(f"{visited}, it is has a cycle")
                return True
            elif visited[neighbour] == 0:
                if dfs(neighbour):
                    return True

        visited[node] = 2
        return False

    for n in range(num_of_nodes):
        if visited[n] == 0:
            if dfs(n):
                return True

print (cyclic_graph(3, graph))
    


graph_str = {
    'A':['B'],
    'B':['C'],
    'C':['A']
}

def cyclic_graph_str(graph = graph_str) -> bool:
    visited = {node: 0 for node in graph}

    def dfs(node):
        visited[node] = 1

        for neighbour in graph[node]:
            if visited[neighbour] == 1:
                print(f"{node}, it is has a cycle")
                return True
            elif visited[neighbour] == 0:
                if dfs(neighbour):
                    return True

        visited[node] = 2
        return False

    for n in graph:
        if visited[n] == 0:
            if dfs(n):
                return True

print (cyclic_graph_str(graph_str))