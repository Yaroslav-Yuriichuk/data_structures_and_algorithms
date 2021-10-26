from tarjan_scc import tarjan_scc

graph1 = [
    [1, 2],
    [0],
    [3],
    [5],
    [4],
    [2]
]


graph2 = [
    [],
    [2],
    [3],
    [1],
    [0, 2, 6],
    [4],
    [5]
]

print(tarjan_scc(graph1))