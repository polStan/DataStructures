def dfs_recursive(graph, node, visited = None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end = " ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    visited = set()  # To track visited nodes
    stack = [start]  # Use a stack for DFS (LIFO)

    while stack:
        node = stack.pop()  # Pop a node from the stack
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node, end=" ")  # Process the node (e.g., print it)

            # Add unvisited neighbors to the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Recursive DFS
print("DFS (Recursive):")
dfs_recursive(graph, 'A')
print()

# Iterative DFS
print("DFS (Iterative):")
dfs_iterative(graph, 'A')