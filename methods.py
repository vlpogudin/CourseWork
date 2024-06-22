from import_library import *


# Метод для построения графа с большим количество вершин
def create_big_graph(right_border, left_border):
    count_node = random.randint(right_border, left_border)  # Задаём количество вершин

    Graph = nx.Graph()  # Создаём как бы мнимыый граф
    Graph.add_nodes_from(range(count_node))  # Добавляем нужное количество вершин

    array_node_number = []  # Создаём массив, в котором будем хранить номера вершин, к которым присоединяем рёбра
    #  добавялем вершины и перемешиваем массив
    for i in range(0, count_node):
        array_node_number.append(i)
    random.shuffle(array_node_number)
    array_node_number.append(array_node_number[0])  # добавялется самая первая вершина, чтобы граф замкнулся

    # добавялем рёбра по очереди от каждой вершины к другой
    for i in range(0, len(array_node_number) - 1):
        first_node_number = array_node_number[i]
        second_node_number = array_node_number[i + 1]
        Graph.add_edge(first_node_number, second_node_number)
    return Graph  # возвращаем получившийся граф


# Метод для рисования исходного графа
def draw_graph_original(graph_original):
    nx.draw(graph_original, with_labels=True, node_size=500, node_color='skyblue',
            font_size=10, font_color='black',
            font_weight='bold', edge_color='gray',
            linewidths=1, pos=nx.circular_layout(graph_original))
    plt.show()


# Метод для рисования графа (с другими позициями вершин)
def draw_graph_changed_position(graph):
    nx.draw(graph, with_labels=True, node_size=500, node_color='skyblue',
            font_size=10, font_color='black',
            font_weight='bold', edge_color='gray',
            linewidths=1, pos=nx.spring_layout(graph))
    plt.show()


# Метод для рисования изоморфного графа (другой цвет вершин)
def draw_graph_isomorphic(graph_isomorphic):
    nx.draw(graph_isomorphic, with_labels=True, node_size=500, node_color='coral',
            font_size=10, font_color='black',
            font_weight='bold', edge_color='gray',
            linewidths=1, pos=nx.circular_layout(graph_isomorphic))
    plt.show()


# Метод для нахождения цикла в графе
def find_cycle(graph_original):
    list_hamiltonians_cycle = networkx.find_cycle(graph_original)  # В графе ищем цикл
    array_hamiltonias_cycle = []  # Создаём массив, в котором будем хранить все вершины из гамильтоного цикла
    for i in range(len(list_hamiltonians_cycle)):  # В цикле будем добавлять вершины из списка в массив
        array_hamiltonias_cycle.append(list_hamiltonians_cycle[i][0])
    return array_hamiltonias_cycle  # Возвращаем полученный массив для дальнейшей работы


# Метод для нахождения гамильтонова цикла в основном графе, просто добавляется первая вершина в массив, чтобы был
# действительно цикл
def find_hamiltonias_cycle_original_graph(graph_original):
    array_hamiltonias_cycle = find_cycle(graph_original)
    array_hamiltonias_cycle.append(array_hamiltonias_cycle[0])  # добавляем самую первую вершину в массив
    return array_hamiltonias_cycle


# Метод печати гамильтонова цикла в графе
def print_hamiltonias_cycle(array_hamiltonias_cycle):
    message_with_hamiltonians_cycle = "Гамильтонов цикл: "
    for i in range(len(array_hamiltonias_cycle)):  # будем идти по циклу и добавлять к строке номер вершины в цикле
        message_with_hamiltonians_cycle += f"{array_hamiltonias_cycle[i]}-"
    return message_with_hamiltonians_cycle[:-1] + '.'  # возвращаем полученное сообщение


# Метод для добавления случайных рёбер в граф, чтобы запутать проверяющего
def add_random_edges(graph_original, factor_count_edge):
    count_nodes = graph_original.number_of_nodes()  # Получаем количество вершин в графе
    count_edges_to_add = ((count_nodes * (count_nodes - 1))
                          / 2 - count_nodes) * factor_count_edge  # Получаем количество рёбер для добавления

    while count_edges_to_add > 0:  # чтобы не было багов при добавлении рёбер
        first_random_node = random.randint(0, count_nodes)
        second_random_node = random.randint(0, count_nodes)
        is_nodes_have_edge = graph_original.has_edge(first_random_node, second_random_node)

        # проверяем есть ли у вершины рёбра и не одинаковые ли first_random_node и second_random_node, иначе может
        # добавиться ребро вершины к самой себе
        if is_nodes_have_edge is False and (first_random_node != second_random_node):
            graph_original.add_edge(first_random_node, second_random_node)
            count_edges_to_add -= 1  # когда добавляем ребро в правильное место
    return graph_original  # возвращаем новый граф с большим количество вершин


# Метод для построения изоморфного графа
def create_isomorphic_graph(graph_original):
    count_nodes = graph_original.number_of_nodes()  # получаем кол-во вершин в оригинальном графе
    changing_name = {}  # словарь, в котором для каждого i-того значения от 0 до кол-ва вершин в оригинальном графе
    # будет новер вершины из изоморфного графа
    array_isomorphic_nodes = []  # массив, в котором храним номера всех вершин в новом графе
    count_cycle = 0  # счётчик, чтобы не допустить ошибок при добавлении графа, потому что могут добавиться вершины
    # с одинаковыми номерами

    while count_cycle < count_nodes:
        isomorphic_node_number = random.randint(0, 1000)  # получаем случайное число для новой вершины
        # в изоморфном графе
        if isomorphic_node_number not in array_isomorphic_nodes:  # если этой вершины ещё нет в массиве
            changing_name[count_cycle] = isomorphic_node_number  # задаём правило соответствия вершин
            array_isomorphic_nodes.append(isomorphic_node_number)  # добавляем её в массив
            count_cycle += 1

    isomorphic_graph = nx.Graph()  # создаём "пустой" изоморфный граф
    isomorphic_graph.add_nodes_from(range(count_nodes))  # добавляем в изоморфный граф столько же вершин,
    # сколько в оригинальном
    isomorphic_graph = nx.relabel_nodes(isomorphic_graph, changing_name)  # заменяем вершины по правилу из словаря

    # в цикле будем соединять вершины так же как в исходном графе, чтобы граф были изоморфными
    for i in range(0, count_nodes):
        list_original_graph_neighbors = [neighbor for neighbor in graph_original.neighbors(i)]  # получаем количество
        # соседей вершины в оригинальном графе
        node_parent = array_isomorphic_nodes[i]  # вершина, к которой будем добавлять рёбра
        for j in range(len(list_original_graph_neighbors)):  # двигаемся по всему списку соседей вершины
            node_child = array_isomorphic_nodes[list_original_graph_neighbors[j]]  # получаем вершину, с которой надо
            # соединить
            isomorphic_graph.add_edge(node_parent, node_child)  # добавляем ребро между вершинами

    return isomorphic_graph, array_isomorphic_nodes  # возвращаем изоморфный граф и массив с циклом в ИГ


# Метод для нахождения гамильтонова цикла в изоморфном графе
def find_hamiltonias_cycle_isomorphic_graph(array_hamiltonias_cycle_original_graph, array_nodes_isomorphic_graph):
    array_hamiltonias_cycle_isomorphic_graph = []  # в массив будет записан гамильтонов циклв  изоморфном графе
    for i in range(len(array_hamiltonias_cycle_original_graph)):  # будем добавлять вершины
        array_hamiltonias_cycle_isomorphic_graph.append(
            array_nodes_isomorphic_graph[array_hamiltonias_cycle_original_graph[i]])  # из массива
        # с вершинами в изоморфном графе будем брать номер по индексу из массива с оригинальными вершинами
    return array_hamiltonias_cycle_isomorphic_graph  # возвращаем оплучившийся цикл в изоморфном графе


# Метод для показа соответствия вершин
def show_compliance_node(array_hamiltonias_cycle_original_graph, array_hamiltonias_cycle_isomorphic_graph):
    s = ''
    for i in range(len(array_hamiltonias_cycle_original_graph)):  # будем идти по циклу и перебирать вершины
        s += (f"Вершина ИС {array_hamiltonias_cycle_original_graph[i]} - "  # ИС - исходный
              f"вершина ИЗ {array_hamiltonias_cycle_isomorphic_graph[i]}.\n")  # ИЗ - изоморфный
    return s[:-2]

