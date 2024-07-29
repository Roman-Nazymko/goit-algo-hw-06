import random
import heapq
import networkx as nx
from graph_creation import create_europe_graph, plot_graph

# Створення графу
G = create_europe_graph()

# Додавання випадкових ваг до ребер
for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)

# Функція для пошуку найкоротшого шляху за допомогою алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація найкоротших шляхів як нескінченність
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]  # Пріоритетна черга

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Огляд сусідів поточного вузла
        for neighbor, attributes in graph[current_vertex].items():
            distance = current_distance + attributes['weight']
            
            # Якщо знайдено коротший шлях до сусіда
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths

# Застосування алгоритму Дейкстри від Франції до всіх інших вузлів
start_node = "France"
shortest_paths_from_france = dijkstra(G, start_node)

# Виведення найкоротших шляхів
print(f"Найкоротші шляхи від {start_node}:")
for destination, distance in shortest_paths_from_france.items():
    print(f"{start_node} -> {destination}: {distance}")

# Візуалізація графу 
plot_graph(G)