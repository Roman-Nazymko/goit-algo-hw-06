from graph_creation import create_europe_graph, plot_graph

# Створення графа
G = create_europe_graph()

# Функція для пошуку шляху за допомогою DFS
def dfs(graph, start, visited=None, path=None, parent=None):
    if visited is None:
        visited = set()
        path = []
    if start in visited:
        return
    visited.add(start)
    print(f"DFS: visited {start}")
    if parent is not None:
        path.append((parent, start))
    for next in graph[start]:
        dfs(graph, next, visited, path, start)
    return path

# Функція для пошуку шляху за допомогою BFS
def bfs(graph, start):
    visited, queue = {start}, [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        print(f"BFS: visited {vertex}")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))
    return path

# Знаходження шляхів за допомогою DFS та BFS
start_node = "France"

dfs_path = dfs(G, start_node)
bfs_path = bfs(G, start_node)

print("\nШлях, знайдений за допомогою DFS:")
print(dfs_path)

print("\nШлях, знайдений за допомогою BFS:")
print(bfs_path)

plot_graph(G)