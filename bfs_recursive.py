def bfs_recursive(graph, queue, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    if not queue:
        return result
    vertex = queue.popleft()
    if vertex not in visited:
        result.append(vertex)  # додаємо у результат
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    return bfs_recursive(graph, queue, visited, result)