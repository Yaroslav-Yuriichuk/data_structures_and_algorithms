from collections import deque

def tarjan_scc(graph):

    n = len(graph)
    current_index = [0,]

    in_stack = [False] * n
    low_link = [n + 1] * n
    ids = [None] * n

    stack = deque()

    scc = []

    def dfs(source):
        ids[source] = current_index[0]
        low_link[source] = current_index[0]
        current_index[0] += 1
        in_stack[source] = True
        stack.append(source)

        for adjacent_vetrex in graph[source]:
            if ids[adjacent_vetrex] is None:
                dfs(adjacent_vetrex)
                low_link[source] = min(low_link[source], low_link[adjacent_vetrex])
            elif in_stack[adjacent_vetrex]:
                low_link[source] = min(low_link[source], low_link[adjacent_vetrex])

        if low_link[source] == ids[source]:
            tmp = stack.pop()
            current_scc = []

            in_stack[tmp] = False
            current_scc.append(tmp)

            while not tmp == source:
                tmp = stack.pop()
                in_stack[tmp] = False
                current_scc.append(tmp)
            
            current_scc.sort()
            scc.append(current_scc)

    for i in range(n):
        if ids[i] is None:
            dfs(i)

    scc.sort()
    return scc        

