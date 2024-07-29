import matplotlib.pyplot as plt
import networkx as nx


def create_europe_graph():
    # Визначення координат країн Європи
    country_coords = {
        "Portugal": (-9, 40),
        "Spain": (-3, 40),
        "France": (2, 46),
        "Belgium": (4, 51),
        "Netherlands": (5.5, 52),
        "Germany": (10, 51),
        "Switzerland": (8, 47),
        "Italy": (12, 42),
        "Austria": (13, 47),
        "Czech Republic": (15, 49),
        "Slovakia": (19, 48.5),
        "Poland": (19, 52),
        "Hungary": (19, 47),
        "Slovenia": (14.5, 46),
        "Croatia": (15.5, 45),
        "Bosnia": (17, 44),
        "Montenegro": (19, 42),
        "Albania": (20, 41),
        "North Macedonia": (21.5, 41.5),
        "Greece": (22, 39),
        "Bulgaria": (25, 42.5),
        "Romania": (25, 46),
        "Serbia": (21, 44),
        "Lithuania": (25, 55),
        "Latvia": (24, 57),
        "Estonia": (25, 59),
        "Belorussia": (27, 53),
        "Ukraine": (30, 49),
        "Moldova": (28, 47),
        "Denmark": (10, 56),
        "Norway": (10, 60),
        "Sweden": (15, 60),
        "Finland": (25, 61),
        "Ireland": (-8, 53),
        "United Kingdom": (-1, 54),
        "Russia": (40, 60)
    }

    # Визначення країн Європи та їх сусідів
    europe_map = {
        "Portugal": ["Spain"],
        "Spain": ["Portugal", "France"],
        "France": ["Spain", "Belgium", "Germany", "Italy", "Switzerland"],
        "Belgium": ["France", "Netherlands", "Germany"],
        "Netherlands": ["Belgium", "Germany"],
        "Germany": ["France", "Belgium", "Netherlands", "Denmark", "Poland", "Czech Republic", "Austria", "Switzerland"],
        "Switzerland": ["France", "Germany", "Austria", "Italy"],
        "Italy": ["France", "Switzerland", "Austria", "Slovenia"],
        "Austria": ["Germany", "Czech Republic", "Slovakia", "Hungary", "Slovenia", "Italy", "Switzerland"],
        "Czech Republic": ["Germany", "Poland", "Slovakia", "Austria"],
        "Slovakia": ["Czech Republic", "Poland", "Ukraine", "Hungary", "Austria"],
        "Poland": ["Germany", "Czech Republic", "Slovakia", "Ukraine", "Belorussia", "Lithuania"],
        "Hungary": ["Austria", "Slovakia", "Ukraine", "Romania", "Serbia", "Croatia", "Slovenia"],
        "Slovenia": ["Italy", "Austria", "Hungary", "Croatia"],
        "Croatia": ["Slovenia", "Hungary", "Serbia", "Bosnia"],
        "Bosnia": ["Croatia", "Serbia", "Montenegro"],
        "Montenegro": ["Bosnia", "Serbia", "Albania"],
        "Albania": ["Montenegro", "Greece", "North Macedonia"],
        "North Macedonia": ["Albania", "Serbia", "Bulgaria", "Greece"],
        "Greece": ["Albania", "North Macedonia", "Bulgaria"],
        "Bulgaria": ["Romania", "Serbia", "North Macedonia", "Greece"],
        "Romania": ["Hungary", "Ukraine", "Moldova", "Bulgaria", "Serbia"],
        "Serbia": ["Hungary", "Romania", "Bulgaria", "North Macedonia", "Albania", "Montenegro", "Bosnia", "Croatia"],
        "Lithuania": ["Latvia", "Belorussia", "Poland"],
        "Latvia": ["Estonia", "Lithuania", "Belorussia"],
        "Estonia": ["Latvia"],
        "Belorussia": ["Poland", "Lithuania", "Latvia", "Russia", "Ukraine"],
        "Ukraine": ["Poland", "Slovakia", "Hungary", "Romania", "Moldova", "Belorussia", "Russia"],
        "Moldova": ["Romania", "Ukraine"],
        "Denmark": ["Germany"],
        "Norway": ["Sweden"],
        "Sweden": ["Norway", "Finland"],
        "Finland": ["Sweden", "Russia"],
        "Ireland": ["United Kingdom"],
        "United Kingdom": ["Ireland"],
        "Russia": ["Finland", "Estonia", "Latvia", "Belorussia", "Ukraine"]
    }
    # Визначити відстань між сусідами (у кілометрах)
    distances = {
        ("Portugal", "Spain"): 1234,
        ("Spain", "France"): 1070,
        ("France", "Belgium"): 305,
        ("France", "Germany"): 451,
        ("France", "Italy"): 1106,
        ("France", "Switzerland"): 577,
        ("Belgium", "Netherlands"): 173,
        ("Belgium", "Germany"): 376,
        ("Netherlands", "Germany"): 558,
        ("Germany", "Denmark"): 650,
        ("Germany", "Poland"): 681,
        ("Germany", "Czech Republic"): 351,
        ("Germany", "Austria"): 676,
        ("Germany", "Switzerland"): 673,
        ("Switzerland", "Austria"): 726,
        ("Switzerland", "Italy"): 697,
        ("Italy", "Austria"): 735,
        ("Italy", "Slovenia"): 320,
        ("Austria", "Czech Republic"): 251,
        ("Austria", "Slovakia"): 76,
        ("Austria", "Hungary"): 243,
        ("Austria", "Slovenia"): 377,
        ("Czech Republic", "Poland"): 511,
        ("Czech Republic", "Slovakia"): 349,
        ("Slovakia", "Ukraine"): 404,
        ("Slovakia", "Hungary"): 201,
        ("Poland", "Ukraine"): 1044,
        ("Poland", "Belorussia"): 683,
        ("Poland", "Lithuania"): 597,
        ("Hungary", "Ukraine"): 1121,
        ("Hungary", "Romania"): 839,
        ("Hungary", "Serbia"): 379,
        ("Hungary", "Croatia"): 259,
        ("Hungary", "Slovenia"): 465,
        ("Slovenia", "Croatia"): 133,
        ("Croatia", "Serbia"): 394,
        ("Croatia", "Bosnia"): 292,
        ("Bosnia", "Serbia"): 281,
        ("Bosnia", "Montenegro"): 194,
        ("Montenegro", "Albania"): 172,
        ("Albania", "Greece"): 447,
        ("Albania", "North Macedonia"): 158,
        ("North Macedonia", "Serbia"): 436,
        ("North Macedonia", "Bulgaria"): 291,
        ("North Macedonia", "Greece"): 271,
        ("Greece", "Bulgaria"): 544,
        ("Bulgaria", "Romania"): 298,
        ("Bulgaria", "Serbia"): 394,
        ("Romania", "Ukraine"): 605,
        ("Romania", "Moldova"): 360,
        ("Romania", "Serbia"): 541,
        ("Serbia", "Lithuania"): 1221,
        ("Lithuania", "Latvia"): 267,
        ("Latvia", "Estonia"): 309,
        ("Lithuania", "Belorussia"): 182,
        ("Latvia", "Belorussia"): 461,
        ("Belorussia", "Russia"): 683,
        ("Ukraine", "Russia"): 755,
        ("Moldova", "Ukraine"): 470,
        ("Denmark", "Norway"): 834,
        ("Denmark", "Sweden"): 285,
        ("Norway", "Sweden"): 486,
        ("Sweden", "Finland"): 546,
        ("Finland", "Russia"): 892,
        ("Ireland", "United Kingdom"): 466
    }

    # Створення графа
    G = nx.Graph()

     # Додавання вершин
    for country, (x, y) in country_coords.items():
        G.add_node(country, pos=(x, y))

    # Додавання ребер з вагами (відстані між країнами)
    for country, neighbors in europe_map.items():
        for neighbor in neighbors:
            distance = distances.get((country, neighbor)) or distances.get((neighbor, country))
            if distance:
                G.add_edge(country, neighbor, weight=distance)

    return G


def plot_graph(G):
    # Отримання позицій вершин
    pos = nx.get_node_attributes(G, 'pos')

    # Побудова графа
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(14, 10))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Мережа Європейських країн")
    plt.show()


if __name__ == "__main__":
    G = create_europe_graph()
    plot_graph(G)