def recursive_dfs(graph, source):

    visited = [False] * len(graph)
    previous = [None] * len(graph)

    def dfs(v):
        visited[v] = True

        for vertice in graph[v]:
            if not visited[vertice]:
                previous[vertice] = v
                dfs(vertice)

    dfs(source)

    return visited, previous