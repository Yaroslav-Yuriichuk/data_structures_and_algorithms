from collections import deque

def iterative_dfs(graph, source):
    visited = [False] * len(graph)
    previous = [None] * len(graph)

    stack = deque()
    stack.append(source)

    while len(stack) > 0:
        vertex = stack.pop()
        visited[vertex] = True

        for adjacent_vertex in graph[vertex]:
            if not visited[adjacent_vertex]:
                stack.append(vertex)
                stack.append(adjacent_vertex)
                previous[adjacent_vertex] = vertex
                break

    return visited, previous

    