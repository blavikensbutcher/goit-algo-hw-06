import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

from networkx import single_source_dijkstra_path

from bfs_recursive import bfs_recursive
from dfs_recursive import dfs_recursive
from dijkstra import dijkstra_r

G = nx.Graph()

cities = [
    'Київ', 'Харків', 'Одеса', 'Дніпро', 'Львів',
    'Запоріжжя', 'Кривий Ріг', 'Миколаїв', 'Маріуполь',
    'Вінниця', 'Херсон', 'Чернігів', 'Полтава',
    'Черкаси', 'Житомир'
]

G.add_nodes_from(cities)

edges_with_weights = [
    ('Київ', 'Харків', 480),
    ('Київ', 'Одеса', 475),
    ('Київ', 'Дніпро', 480),
    ('Київ', 'Львів', 540),
    ('Київ', 'Запоріжжя', 520),
    ('Київ', 'Кривий Ріг', 430),
    ('Київ', 'Миколаїв', 480),
    ('Київ', 'Маріуполь', 750),
    ('Київ', 'Вінниця', 270),
    ('Київ', 'Херсон', 550),
    ('Київ', 'Чернігів', 150),
    ('Київ', 'Полтава', 340),
    ('Київ', 'Черкаси', 190),
    ('Київ', 'Житомир', 140),

    ('Львів', 'Вінниця', 370),
    ('Львів', 'Чернівці', 270),
    ('Львів', 'Житомир', 470),
    ('Дніпро', 'Запоріжжя', 85),
    ('Дніпро', 'Кривий Ріг', 150),
    ('Дніпро', 'Полтава', 160),
    ('Одеса', 'Миколаїв', 130),
    ('Миколаїв', 'Херсон', 65),
    ('Харків', 'Полтава', 150),
    ('Чернігів', 'Житомир', 320),
    ('Черкаси', 'Кривий Ріг', 330),
]

for city1, city2, distance in edges_with_weights:
    G.add_edge(city1, city2, weight=distance)


pos = nx.spring_layout(G, seed=42)  

plt.figure(figsize=(12, 10))


nx.draw_networkx_nodes(G, pos, node_size=800, node_color='lightblue')


nx.draw_networkx_edges(G, pos, width=2)


nx.draw_networkx_labels(G, pos, font_size=12, font_family='Arial')


edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)


deep_down = dfs_recursive(graph=G, vertex='Київ')

bfs_walk = bfs_recursive(G, deque(['Київ']))

dijkstra = single_source_dijkstra_path(G, source='Київ', weight='weight')

dijkstra_realization = dijkstra_r(G, 'Київ')




# Стилізація для консолі (кольори)
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Вивід результатів
print(f'\n{BOLD}{BLUE}=== Глибина графу DFS ==={RESET}')
print(f'{GREEN}{deep_down}{RESET}')

print(f'\n{BOLD}{MAGENTA}=== Глибина графу BFS ==={RESET}')
print(f'{YELLOW}{bfs_walk}{RESET}')

print(f'\n{BOLD}{CYAN}=== Найкоротші шляхи за алгоритмом Дейкстри (від Києва) ==={RESET}')
for target_city, path in dijkstra.items():
    if target_city != 'Київ':  # Не виводити шлях до себе
        print(f"{BOLD}{target_city}{RESET}: {path}")
        
        print(f'\n{BOLD}{CYAN}=== Найкоротші шляхи за алгоритмом Дейкстри (від Києва) Реалізація ==={RESET}')




plt.title('Граф головних міст України з вагами в км', fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()