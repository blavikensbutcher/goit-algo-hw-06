def dijkstra_r(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    previous_nodes = {vertex: None for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]["weight"]
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        unvisited.remove(current_vertex)

    paths = {}
    for vertex in graph.nodes:
        path = []
        current = vertex
        while current is not None:
            path.insert(0, current)
            current = previous_nodes[current]
        paths[vertex] = path

    return paths
