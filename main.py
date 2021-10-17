from recursive_dfs import recursive_dfs

graph = [
    [4],
    [2, 5],
    [1, 5],
    [7],
    [0, 6],
    [1, 2, 6],
    [4, 5],
    [3]
]


visited, previous = recursive_dfs(graph, 1)

print(visited)
print(previous)