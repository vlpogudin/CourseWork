from import_library import *


# Метод для построения графа с большим количество вершин
def create_big_graph(right_border, left_border):
    count_node = random.randint(right_border, left_border)#задаём количество вершин

    Graph = nx.Graph()#создаём как бы мнимыый граф
    Graph.add_nodes_from(range(count_node))#добавляем нужное количество вершин

    array_node_number = []#создаём массив, в котором будем хранить номера вершин, к которым присоединяем рёбра
    #добавялем вершины и перемешиваем массив
    for i in range(0, count_node):
        array_node_number.append(i)
    random.shuffle(array_node_number)
    array_node_number.append(array_node_number[0])#добавялется самая первая вершина, чтобы граф замкнулся

    #добавялем рёбра по очереди от каждой вершины к другой
    for i in range(0, len(array_node_number) - 1):
        first_node_number = array_node_number[i]
        second_node_number = array_node_number[i + 1]
        Graph.add_edge(first_node_number, second_node_number)
    return Graph#возвращаем получившийся граф


# Метод для рисования исходного графа
def draw_graph_original(graph_original):
    nx.draw(graph_original, with_labels=True, node_size=500, node_color='skyblue',
            font_size=10, font_color='black',
            font_weight='bold', edge_color='gray',
            linewidths=1, pos=nx.circular_layout(graph_original))
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
    list_hamiltonians_cycle = networkx.find_cycle(graph_original)
    array_hamiltonias_cycle = []
    for i in range(len(list_hamiltonians_cycle)):
        array_hamiltonias_cycle.append(list_hamiltonians_cycle[i][0])
    return array_hamiltonias_cycle


# Метод для нахождения гамильтонова цикла в основном графе
def find_hamiltonias_cycle_original_graph(graph_original):
    array_hamiltonias_cycle = find_cycle(graph_original)
    array_hamiltonias_cycle.append(array_hamiltonias_cycle[0])
    return array_hamiltonias_cycle


# Метод печати гамильтонова цикла в графе
def print_hamiltonias_cycle(array_hamiltonias_cycle):
    message_with_hamiltonians_cycle = "Гамильтонов цикл: "
    for i in range(len(array_hamiltonias_cycle)):
        message_with_hamiltonians_cycle += f"{array_hamiltonias_cycle[i]}-"
    return message_with_hamiltonians_cycle[:-1] + '.'


# Метод для добавления случайных рёбер в граф, чтобы запутать проверяющего
def add_random_edges(graph_original, factor_count_edge):
    count_nodes = graph_original.number_of_nodes()#получаем количество вершин в графе
    count_edges_to_add = ( (count_nodes * ( count_nodes - 1 )) / 2 - count_nodes ) * factor_count_edge#получаем количество
        #рёбер для добавления

    while (count_edges_to_add > 0):
        first_random_node = random.randint(0,count_nodes)
        second_random_node = random.randint(0, count_nodes)
        is_nodes_have_edge = graph_original.has_edge(first_random_node,second_random_node)

        if is_nodes_have_edge == False and (first_random_node != second_random_node):
            graph_original.add_edge(first_random_node,second_random_node)
            count_edges_to_add -= 1
    return graph_original


# Метод для построения изоморфного графа
def create_isomorphic_graph(graph_original):
    count_nodes = graph_original.number_of_nodes()
    changing_name = {}
    array_isomorphic_nodes = []
    count_cycle = 0

    while count_cycle < count_nodes:
        isomorphic_node_number = random.randint(0, 1000)
        if isomorphic_node_number not in array_isomorphic_nodes:
            changing_name[count_cycle] = isomorphic_node_number
            array_isomorphic_nodes.append(isomorphic_node_number)
            count_cycle += 1

    isomorphic_graph = nx.Graph()
    isomorphic_graph.add_nodes_from(range(count_nodes))
    isomorphic_graph = nx.relabel_nodes(isomorphic_graph, changing_name)

    for i in range(0,count_nodes):
        list_original_graph_neighbors = [neighbor for neighbor in graph_original.neighbors(i)]
        node_parent = array_isomorphic_nodes[i]
        for j in range(len(list_original_graph_neighbors)):
            node_child = array_isomorphic_nodes[list_original_graph_neighbors[j]]
            isomorphic_graph.add_edge(node_parent, node_child)

    return isomorphic_graph, array_isomorphic_nodes

# Метод для нахождения гамильтонова цикла в изоморфном графе
def find_hamiltonias_cycle_isomorphic_graph(array_hamiltonias_cycle_original_graph, array_nodes_isomorphic_graph):
    array_hamiltonias_cycle_isomorphic_graph = []
    for i in range(len(array_hamiltonias_cycle_original_graph)):
        array_hamiltonias_cycle_isomorphic_graph.append(array_nodes_isomorphic_graph[array_hamiltonias_cycle_original_graph[i]])
    return array_hamiltonias_cycle_isomorphic_graph

# Метод для показа соответствия вершин
def show_compliance_node(array_hamiltonias_cycle_original_graph, array_hamiltonias_cycle_isomorphic_graph):
    s = ''
    for i in range(len(array_hamiltonias_cycle_original_graph)):
        s += (f"Вершина ИС {array_hamiltonias_cycle_original_graph[i]} соответственна "
              f"вершине ИЗ {array_hamiltonias_cycle_isomorphic_graph[i]}.\n")
    return s[:-2]