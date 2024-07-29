from graph_creation import create_europe_graph, plot_graph

# Створення графа
G = create_europe_graph()

# Аналіз основних характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())
average_degree = round(sum(degree.values()) / num_nodes, 2)

print("Кількість вершин:", num_nodes)
print("Кількість ребер:", num_edges)
print("Ступінь кожної вершини:", degree)
print("Середній ступінь вершин:", average_degree)

plot_graph(G)