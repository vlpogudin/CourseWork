from import_library import *


# region Создание графов
# Метод для построения графа с большим количество вершин
def create_big_graph(right_border, left_border):
    count_node = random.randint(right_border, left_border)  # Задаём количество вершин

    graph = nx.Graph()  # Создаём как бы мнимый граф
    graph.add_nodes_from(range(count_node))  # Добавляем нужное количество вершин

    array_node_number = []  # Создаём массив, в котором будем хранить номера вершин, к которым присоединяем рёбра
    #  Добавляем вершины и перемешиваем массив
    for i in range(0, count_node):
        array_node_number.append(i)
    random.shuffle(array_node_number)
    array_node_number.append(array_node_number[0])  # Добавляется самая первая вершина, чтобы граф замкнулся

    # Добавляем рёбра по очереди от каждой вершины к другой
    for i in range(0, len(array_node_number) - 1):
        first_node_number = array_node_number[i]
        second_node_number = array_node_number[i + 1]
        graph.add_edge(first_node_number, second_node_number)
    return graph  # Возвращаем получившийся граф


# Метод для построения изоморфного графа
def create_isomorphic_graph(graph_original):
    count_nodes = graph_original.number_of_nodes()  # Получаем кол-во вершин в оригинальном графе
    changing_name = {}  # Словарь, в котором для каждого i-того значения от 0 до кол-ва вершин в оригинальном графе
    # будет номер вершины из изоморфного графа
    array_isomorphic_nodes = []  # Массив, в котором храним номера всех вершин в новом графе
    array_binary_search = []  # Массив, в котором храним номера вершин для бинарного поиска
    count_cycle = 0  # Счётчик, чтобы не допустить ошибок при добавлении графа, потому что могут добавиться вершины
    # С одинаковыми номерами

    while count_cycle < count_nodes:
        isomorphic_node_number = random.randint(0, count_nodes - 1)  # Получаем случайное число для новой вершины
        # в изоморфном графе

        array_binary_search = bubble_sort(array_binary_search)
        index = binary_search(array_binary_search, 0, len(array_isomorphic_nodes) - 1, isomorphic_node_number)
        if index == -1:
            changing_name[count_cycle] = isomorphic_node_number  # Задаём правило соответствия вершин
            array_binary_search.append(isomorphic_node_number)
            array_isomorphic_nodes.append(isomorphic_node_number)  # Добавляем её в массив
            count_cycle += 1

    isomorphic_graph = nx.Graph()  # Создаём "пустой" изоморфный граф
    isomorphic_graph.add_nodes_from(range(count_nodes))  # Добавляем в изоморфный граф столько же вершин,
    # сколько в оригинальном
    isomorphic_graph = nx.relabel_nodes(isomorphic_graph, changing_name)  # Заменяем вершины по правилу из словаря

    # В цикле будем соединять вершины так же как в исходном графе, чтобы граф были изоморфными
    for i in range(0, count_nodes):
        list_original_graph_neighbors = [neighbor for neighbor in graph_original.neighbors(i)]  # Получаем количество
        # соседей вершины в оригинальном графе
        node_parent = array_isomorphic_nodes[i]  # Вершина, к которой будем добавлять рёбра
        for j in range(len(list_original_graph_neighbors)):  # Двигаемся по всему списку соседей вершины
            node_child = array_isomorphic_nodes[list_original_graph_neighbors[j]]  # Получаем вершину, с которой надо
            # соединить
            isomorphic_graph.add_edge(node_parent, node_child)  # Добавляем ребро между вершинами

    return isomorphic_graph, array_isomorphic_nodes  # Возвращаем изоморфный граф и массив с циклом в ИГ


# Метод для создания графа, в котором мы не знаем гамильтонов цикл
def create_false_graph(right_border, left_border):
    count_node = random.randint(right_border, left_border)  # Задаём количество вершин

    graph = nx.Graph()  # Создаём как бы мнимый граф
    graph.add_nodes_from(range(count_node))  # Добавляем нужное количество вершин

    array_node_number = []  # Создаём массив, в котором будем хранить номера вершин, к которым присоединяем рёбра
    # Добавляем вершины и перемешиваем массив
    for i in range(0, count_node):
        array_node_number.append(i)
    random.shuffle(array_node_number)

    # Добавляем рёбра по очереди от каждой вершины к другой
    for i in range(0, len(array_node_number) - 1):
        first_node_number = array_node_number[i]
        second_node_number = array_node_number[i + 1]
        graph.add_edge(first_node_number, second_node_number)

    return graph  # Возвращаем получившийся граф


# Метод для создания изоморфного графа для оригинального без гамильтонова цикла
def create_isomorphic_false_graph(original_graph):
    count_nodes = original_graph.number_of_nodes()
    isomorphic_graph = nx.Graph()  # Создаем как бы мнимый граф
    isomorphic_graph.add_nodes_from(range(count_nodes))  # Граф с таким же количеством вершин

    array_node_number = []  # Создаём массив, в котором будем хранить номера вершин, к которым присоединяем рёбра
    #  Добавляем вершины и перемешиваем массив
    for i in range(0, count_nodes):
        array_node_number.append(i)
    random.shuffle(array_node_number)
    array_node_number.append(array_node_number[0])

    # Добавляем рёбра по очереди от каждой вершины к другой
    for i in range(0, len(array_node_number) - 1):
        first_node_number = array_node_number[i]
        second_node_number = array_node_number[i + 1]
        isomorphic_graph.add_edge(first_node_number, second_node_number)

    add_random_edges(isomorphic_graph, 0.4)

    return isomorphic_graph, array_node_number  # Возвращаем получившийся граф


# Метод для добавления случайных рёбер в граф, чтобы запутать проверяющего
def add_random_edges(graph_original, factor_count_edge):
    count_nodes = graph_original.number_of_nodes()  # Получаем количество вершин в графе
    count_edges_to_add = ((count_nodes * (count_nodes - 1))
                          / 2 - count_nodes) * factor_count_edge  # Получаем количество рёбер для добавления

    while count_edges_to_add > 0:  # Чтобы не было багов при добавлении рёбер
        first_random_node = random.randint(0, count_nodes - 1)
        second_random_node = random.randint(0, count_nodes - 1)
        is_nodes_have_edge = graph_original.has_edge(first_random_node, second_random_node)

        # Проверяем есть ли у вершины рёбра и не одинаковые ли first_random_node и second_random_node, иначе может
        # добавиться ребро вершины к самой себе
        if is_nodes_have_edge is False and (first_random_node != second_random_node):
            graph_original.add_edge(first_random_node, second_random_node)
            count_edges_to_add -= 1  # Когда добавляем ребро в правильное место
    return graph_original  # Возвращаем новый граф с большим количество вершин
# endregion Создание графов


# region Рисование графа
# Метод для рисования исходного графа
def draw_graph_original(graph_original):
    # Рисуем и показываем граф
    nx.draw(graph_original, with_labels=True, node_size=500, node_color='skyblue',
            font_size=10, font_color='black',
            font_weight='bold', edge_color='gray',
            linewidths=1, pos=nx.circular_layout(graph_original))
    plt.show()


# Метод для рисования графа (с другими позициями вершин)
def draw_graph_changed_position(graph):
    # Рисуем и показываем граф
    nx.draw(graph, with_labels=True, node_size=500, node_color='skyblue',
            font_size=10, font_color='black',
            font_weight='bold', edge_color='gray',
            linewidths=1, pos=nx.spring_layout(graph))
    plt.show()


# Метод для рисования изоморфного графа (другой цвет вершин)
def draw_graph_isomorphic(graph_isomorphic):
    # Рисуем и показываем граф
    nx.draw(graph_isomorphic, with_labels=True, node_size=500, node_color='coral',
            font_size=10, font_color='black',
            font_weight='bold', edge_color='gray',
            linewidths=1, pos=nx.circular_layout(graph_isomorphic))
    plt.show()
# endregion Рисование графа


# region Поиск гамильтонова цикла в графе
# Метод для нахождения цикла в оригинальном графе
def find_cycle(graph_original):
    list_hamiltonians_cycle = networkx.find_cycle(graph_original)  # В графе ищем цикл
    array_hamiltonias_cycle = []  # Создаём массив, в котором будем хранить все вершины из гамильтоного цикла
    for i in range(len(list_hamiltonians_cycle)):  # В цикле будем добавлять вершины из списка в массив
        array_hamiltonias_cycle.append(list_hamiltonians_cycle[i][0])
    return array_hamiltonias_cycle  # Возвращаем полученный массив для дальнейшей работы


# Метод для нахождения гамильтонова цикла в основном графе, просто добавляется первая вершина
# в массив, чтобы был действительно цикл
def find_hamiltonias_cycle_original_graph(graph_original):
    array_hamiltonias_cycle = find_cycle(graph_original)
    array_hamiltonias_cycle.append(array_hamiltonias_cycle[0])  # Добавляем самую первую вершину в массив
    return array_hamiltonias_cycle


# Метод для нахождения гамильтонова цикла в изоморфном графе
def find_hamiltonias_cycle_isomorphic_graph(array_hamiltonias_cycle_original_graph, array_nodes_isomorphic_graph):
    array_hamiltonias_cycle_isomorphic_graph = []  # В массив будет записан гамильтонов цикл в изоморфном графе
    for i in range(len(array_hamiltonias_cycle_original_graph)):  # Будем добавлять вершины
        array_hamiltonias_cycle_isomorphic_graph.append(
            array_nodes_isomorphic_graph[array_hamiltonias_cycle_original_graph[i]])  # Из массива
        # С вершинами в изоморфном графе будем брать номер по индексу из массива с оригинальными вершинами
    return array_hamiltonias_cycle_isomorphic_graph  # Возвращаем получившийся цикл в изоморфном графе


# Проверка на корректный гамильтонов цикл
def check_hamiltonias_cycle(array_hamiltonias_cycle, graph):
    for i in range(len(array_hamiltonias_cycle)-1):
        node_current = array_hamiltonias_cycle[i]
        node_next = array_hamiltonias_cycle[i+1]
        array_neighbors = [n for n in graph.neighbors(node_current)]
        if node_next not in array_neighbors:
            return False
    return True
# endregion Поиск гамильтонова цикла в графе


# region Методы под кнопки
# Метод для показа соответствия вершин
def show_compliance_node(array_hamiltonias_cycle_original_graph, array_hamiltonias_cycle_isomorphic_graph):
    hamiltonias_cycle_dict = {}  # Создадим словарь, в который будем добавлять вершины по правилу (вершина ИС :
    # вершина ИЗ)
    if len(array_hamiltonias_cycle_original_graph) == 0:
        array_hamiltonias_cycle_original_graph = random.sample(range(len(array_hamiltonias_cycle_isomorphic_graph)),
                                                               len(array_hamiltonias_cycle_isomorphic_graph))

    for i in range(len(array_hamiltonias_cycle_original_graph)):  # Заполняем полученный словарь, длина - 1,
        # Чтобы не было повтора с 1 вершиной
        hamiltonias_cycle_dict[array_hamiltonias_cycle_original_graph[i]] = array_hamiltonias_cycle_isomorphic_graph[i]

    # Выполняем сортировку массива пузырьком
    array = array_hamiltonias_cycle_original_graph
    array = bubble_sort(array)

    s = ''
    for i in range(1, len(array)):  # Будем идти по циклу и перебирать вершины
        s += (f"Вершина ИС {array[i]} - "  # ИС - исходный
              f"вершина ИЗ {hamiltonias_cycle_dict[array[i]]}.\n")
        # ИЗ - изоморфный
    return s[:-1]


# Метод для сравнения двух графов, путём соответствия вершин
def compare_graphs(original_graph, isomorphic_graph):
    list_nodes_original = list(original_graph.nodes)
    list_nodes_isomorphic = list(isomorphic_graph.nodes)
    count_cycle = 0
    count_nodes = original_graph.number_of_nodes()

    while count_cycle < count_nodes:
        node1 = list_nodes_original[count_cycle]
        node2 = list_nodes_isomorphic[count_cycle]
        len_array1 = len([n for n in original_graph.neighbors(node1)])
        len_array2 = len([n for n in isomorphic_graph.neighbors(node2)])
        if len_array2 != len_array1:
            return False
        else:
            count_cycle += 1

    return True
# endregion Методы под кнопки


# region Вспомогательные методы
# Метод для бинарного поиска элемента в массиве
def binary_search(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2  # Ищем центр массива

        # Если же мы нашли X
        if arr[mid] == x:
            return mid

        # Если Х больше, чем элемент в середине массива
        elif arr[mid] < x:
            low = mid + 1

        # Если Х меньше, чем элемент в середине массива
        else:
            high = mid - 1

    # Если мы дошли до этого момента, то элемент не найден
    return -1


# Метод для сортировки массива методом пузырька
def bubble_sort(array_graph):
    lenght_array_original_graph = len(array_graph)  # Запоминаем длину массива
    for i in range(lenght_array_original_graph - 1):  # Перебор элементов и попарная сортировка
        for j in range(0, lenght_array_original_graph - i - 1):
            if array_graph[j] > array_graph[j + 1]:
                array_graph[j], array_graph[j + 1] = array_graph[j + 1], array_graph[j]
    return array_graph


# Метод печати гамильтонова цикла в графе
def print_hamiltonias_cycle(array_hamiltonias_cycle):
    message_with_hamiltonians_cycle = ""
    for i in range(len(array_hamiltonias_cycle)):  # будем идти по циклу и добавлять к строке номер вершины в цикле
        message_with_hamiltonians_cycle += f"{array_hamiltonias_cycle[i]}-"
    return message_with_hamiltonians_cycle[:-1] + '.'  # возвращаем полученное сообщение
# endregion Вспомогательные методы

#testmerge
