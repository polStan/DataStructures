from collections import deque

def dfs(graph, start, visited = None, dfs_order = None):
    if visited is None: # Will check if the node visited is None
        visited = set()
    if dfs_order is None:
        dfs_order = []

    visited.add(start) 
    dfs_order.append(start)

    if start < len(graph):  # Ensures the start node is within the graph bounds
        for neighbor in graph[start]: # Will check each neighbor in the graph
            if neighbor not in visited: # If the neighbor is not in visited, dfs is called with the graph, neighbor, visited, and the list of numbers
                dfs(graph, neighbor, visited, dfs_order)

    return dfs_order # Will return the list containing the depth first traversal nodes

def bfs(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes  # Keeps track of visited nodes by index 
    queue = deque([start])  # Initializes a queue with the index containing the numbers that are part of graph
    visited[start] = True # Assigning the first node as True
    bfs_order = [start]  # stores nodes (indices) in BFS traversal order

    while queue:
        current_node = queue.popleft()  # Dequeues the node and assigns it to the current node

        # Explores neighbors of the current node
        if current_node < num_nodes:  # Ensures the current node is within bounds
            for neighbor in graph[current_node]:
                if 0 <= neighbor < num_nodes and not visited[neighbor]: #If 0 is less than or equal to the nighbor and less than the number of nodes in the graph, and the node does not have children, that neigbor is appended into the queue and appended back to the list
                    visited[neighbor] = True # Marking the visited neighbor to true
                    queue.append(neighbor) # Appending the neighbor into the queue
                    bfs_order.append(neighbor) # appending the neighbor nodes into the traversal list.

    return bfs_order # Will return the breadth first traversal nodes


#graph_list = [[1, 2],[0, 3, 4],[0, 5],[1],[1, 5],[2, 4]]
#graph_list = [[1], [0, 2, 3], [1], [1]]
#graph_list = [[1, 2], [0, 3], [0], [1, 4, 5], [3], [3]]
#graph_list = [[1], [0, 2], [1], [], [5], [4]]
#graph_list = [[1, 2, 3], [0], [0], [0]]
#graph_list = [[1, 2], [0, 3], [0, 4], [1], [2]]
graph_list = [[1, 2], [0, 3, 4], [0], [1], [1, 5],[4]]
#graph_list = [[1, 2], [0, 3, 4], [0, 5], [1], [1, 5],[2, 4]]

start_node = 0
dfs_result = dfs(graph_list, start_node)
bfs_result = bfs(graph_list, start_node)
print("graph =", graph_list)
print("start_node =", start_node)
print("expected_dfs_result = ", dfs_result)
print("expected_bfs_result = ", bfs_result)
    








