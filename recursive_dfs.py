def recursive_dfs(graph, source):
    visited = [False] * len(graph)
    previous = [None] * len(graph)

    def dfs(v):
        visited[v] = True

        for adjecent_vertex in graph[v]:
            if not visited[adjecent_vertex]:
                previous[adjecent_vertex] = v
                dfs(adjecent_vertex)

    dfs(source)

    return visited, previous
