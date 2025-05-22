from collections import deque

def bfs(graph, s):
    visited = set()
    queue = deque([s])
    visited.add(s)

    while queue:
        node = queue.popleft()
        print(node, end = " ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']

}

bfs(graph, 'A')
print("\n")
bfs(graph, 'B')
print("\n")
bfs(graph, 'C')
print("\n")
bfs(graph, 'D')
print("\n")
bfs(graph, 'E')
print("\n")
bfs(graph, 'F')
print("\n")