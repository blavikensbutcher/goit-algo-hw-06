def dfs_recursive(graph, vertex, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(vertex)
    result.append(vertex)

    for neighbor in graph.neighbors(vertex):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)

    return result
