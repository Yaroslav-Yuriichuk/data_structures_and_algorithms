from recursive_dfs import recursive_dfs
from iterative_dfs import iterative_dfs

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


visited1, previous1 = recursive_dfs(graph, 1)
visited2, previous2 = iterative_dfs(graph, 1)

print(visited1)
print(previous1)
print()
print(visited2)
print(previous2)