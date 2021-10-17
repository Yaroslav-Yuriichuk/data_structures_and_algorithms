from collections import deque

def iterative_dfs(graph, source):
    visited = [False] * len(graph)
    previous = [None] * len(graph)
    start_index = [0] * len(graph)

    stack = deque()
    stack.append(source)

    while len(stack) > 0:
        vertex = stack.pop()
        visited[vertex] = True

        for index in range(start_index[vertex], len(graph[vertex])):
            adjacent_vertex = graph[vertex][index]

            if not visited[adjacent_vertex]:
                stack.append(vertex)
                stack.append(adjacent_vertex)
                previous[adjacent_vertex] = vertex
                start_index[vertex] = index
                break

    return visited, previous
