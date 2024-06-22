import sys  # sys нужен для передачи argv в QApplication
import keyboard
import webbrowser
import os

import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize

import gui  # Это наш конвертированный файл дизайна
import methods
import networkx as nx


class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле gui.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        # Создание и хранение исходного графа
        self.orig_hamiltonias_cycle = []
        self.graph_original = self.create_original_graph()

        # Хранение узлов изоморфного графа
        self.isomorph_hamiltonias_cycle = []

        # Блокируем кнопки, чтобы их можно было нажать только после вывода всей информации
        self.block_buttons()

        # Начало диалога
        self.print_welcome_messages()

        # Нажатие на кнопку "Соотношение сторон"
        self.pb_VertexRatio.clicked.connect(self.push_vertex_ratio)

        # Нажатие на кнопку "Гамильтонов цикл"
        self.pb_Cycle.clicked.connect(self.PushCycle)

        # Нажатие на кнопку "Новый диалог"
        self.pb_NewDialog.clicked.connect(self.ClearWidgets)

        # Добавляем горячую клавишу для открытия руководства пользователя
        keyboard.add_hotkey("f1", self.open_documentation)

    # region Начало диалога
    # Печать начальных сообщений и исходного графа
    def print_welcome_messages(self):
        # Создаем и печатаем оригинальный граф
        qimg_orig = self.save_original_graph()
        self.print_original_graph(qimg_orig)

        self.timer = QtCore.QTimer()  # Создаем таймер
        self.timer.timeout.connect(self.print_next_messages)  # Подключаем печать следующего сообщения к таймеру
        self.timer.start(1000)  # Ставим таймер с интервалом в 1 секунду
        self.message_index = 0  # Создаем счетчик для отслеживания текущего сообщения

    # Печать следующего сообщения по таймеру
    def print_next_messages(self):
        # Создаем список с сообщениями
        messages = [
            "Доказывающий: Я знаю гамильтонов цикл в исходном графе.",
            "Проверяющий: Докажи это!",
            "Доказывающий: Я не буду показывать тебе исходный граф. Я лучше докажу тебе это, используя изоморфный граф."
        ]
        if self.message_index < len(messages):
            # Выводим текущее сообщение в текстовое поле
            self.te_DialogWindow.append(messages[self.message_index])
            # Увеличиваем счетчик, чтобы вывести следующее сообщение
            self.message_index += 1
        else:
            # Если все сообщения выведены, останавливаем таймер
            self.timer.stop()
            self.pb_Cycle.setEnabled(True)  # Разблокируем кнопки после вывода всех сообщений
            self.pb_VertexRatio.setEnabled(True)
    # endregion

    # region Обработка нажатия на кнопку "Соответствие вершин"
    # Обработка нажатия на кнопку "Соответствие вершин"
    def push_vertex_ratio(self):
        # Блокируем кнопки
        self.block_buttons()

        # Печать запроса проверяющего
        self.print_question_vertex_ratio()

        # Создаем и печатаем изоморфный граф
        qimg_isomorph = self.create_and_safe_isomorphic_graph()
        self.print_isomorphic_graph(qimg_isomorph)

        # Спим, изображая раздумья доказывающего
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.print_answer_vertex_ratio)  # Подключаем к нужному слоту
        self.timer.setSingleShot(True)  # Выполнить только один раз
        self.timer.start(1000)

    # Печать вопроса проверяющего
    def print_question_vertex_ratio(self):
        # Печать запроса проверяющего
        self.te_DialogWindow.append("Проверяющий: Покажи соответствие вершин.")

    # Печать ответа доказывающего
    def print_answer_vertex_ratio(self):
        # Печать ответа доказывающего
        self.te_DialogWindow.append("Доказывающий: Демонстрирую соответствие вершин на графе.")
        # Печать соответствия вершин
        vertex_ratio = methods.show_compliance_node(self.orig_hamiltonias_cycle, self.isomorph_hamiltonias_cycle)
        self.te_DialogWindow.append(vertex_ratio)
        # Возвращаем кнопкам активное состояние
        self.enable_buttons()
    # endregion

    # region Обработка нажатия на кнопку "Гамильтонов цикл"
    # Обработка нажатия на кнопку "Гамильтонов цикл"
    def PushCycle(self):
        # Блокируем кнопки
        self.block_buttons()

        # Печать запроса проверяющего
        self.print_question_cycle()

        # Создаем и печатаем изоморфный граф
        qimg_isomorph = self.create_and_safe_isomorphic_graph()
        self.print_isomorphic_graph(qimg_isomorph)

        # Спим, изображая раздумья доказывающего
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.print_answer_cycle)  # Подключаем к нужному слоту
        self.timer.setSingleShot(True)  # Выполнить только один раз
        self.timer.start(1000)

    # Печать вопроса проверяющего
    def print_question_cycle(self):
        # Печать запроса проверяющего и ответа доказывающего
        self.te_DialogWindow.append("Проверяющий: Покажи гамильтонов цикл.")

    # Печать ответа доказывающего
    def print_answer_cycle(self):
        # Печать ответа доказывающего
        self.te_DialogWindow.append("Доказывающий: Показываю гамильтонов цикл в изоморфном графе.")
        # Печать гамильтонова графа
        hamiltonias_cycle = methods.print_hamiltonias_cycle(self.isomorph_hamiltonias_cycle)
        self.te_DialogWindow.append(hamiltonias_cycle)
        # Возвращаем кнопкам активное состояние
        self.enable_buttons()

    # endregion

    # region Обработка нажатия на кнопку "Новый диалог"
    # Обработка кнопки "Новый диалог" (очистка всех виджетов)
    def ClearWidgets(self):
        # Блокируем кнопки
        self.block_buttons()
        # Очистка диалогового окна
        self.te_DialogWindow.clear()
        # Создаем новый исходный граф
        self.graph_original = self.create_original_graph()
        # Вызов функции печати начальных сообщений диалога
        self.print_welcome_messages()
    # endregion

    # region Работа со вспомогательной документацией
    # Открытие руководства пользователя
    def open_documentation(self):
        help_file = 'C:\\Users\\pogud\\OneDrive\\Desktop\\HSE\\Курсовой проект\\Руководство пользователя.docx'
        if os.path.exists(help_file):
            webbrowser.open('file://' + os.path.realpath(help_file))
        else:
            print("Файл не найден")
    # endregion

    # region Работа с оригинальным графом
    # Создание исходного графа
    def create_original_graph(self):
        # Создание нового (исходного графа)
        graph_original = methods.create_big_graph(20, 30)

        # Запоминаем гамильтонов цикл в исходном графе
        self.orig_hamiltonias_cycle = methods.find_hamiltonias_cycle_original_graph(graph_original)

        # Добавляем ребра в граф
        graph_original = methods.add_random_edges(graph_original, 0.4)
        return graph_original

    # Сохранение исходного графа
    def save_original_graph(self):
        # Создание объекта фигуры и объекта оси
        fig, ax = plt.subplots(figsize=(8, 8))

        # Печать графа для запоминания картинки
        nx.draw(self.graph_original, with_labels=True, node_size=500, node_color='skyblue',
                font_size=10, font_color='black',
                font_weight='bold', edge_color='gray',
                linewidths=1, pos=nx.circular_layout(self.graph_original))

        # Сохраняем файл картинки с графом
        fig.savefig('OriginalGraph.png')
        plt.close(fig)
        # Считываем картинку и запоминаем её как QPixmap
        qimg = QPixmap('OriginalGraph.png')
        qimg = qimg.scaled(QSize(720, 580), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        return qimg

    # Вывод исходного графа в текстовое окно GraphImage
    def print_original_graph(self, qimg):
        # Устанавливаем в окно картинку
        self.lb_OrigGraphImage.setPixmap(qimg)
    # endregion

    # region Работа с изоморфным графом
    # Создание и печать изоморфного графа
    def create_and_safe_isomorphic_graph(self):
        # Создание объекта фигуры и объекта оси
        fig, ax = plt.subplots(figsize=(8, 8))

        # Создаем изоморфный граф
        graph_isomorphic, list = methods.create_isomorphic_graph(self.graph_original)
        self.isomorph_hamiltonias_cycle = methods.find_hamiltonias_cycle_isomorphic_graph(self.orig_hamiltonias_cycle, list)

        # Печать графа для запоминания картинки
        nx.draw(graph_isomorphic, with_labels=True, node_size=500, node_color='coral',
                font_size=10, font_color='black',
                font_weight='bold', edge_color='gray',
                linewidths=1, pos=nx.circular_layout(graph_isomorphic))

        # Сохраняем файл картинки с графом
        fig.savefig('IsomorphicGraph.png')
        plt.close(fig)
        # Считываем картинку и запоминаем её как QPixmap
        qimg_isomorph = QPixmap('IsomorphicGraph.png')
        qimg_isomorph = qimg_isomorph.scaled(QSize(720, 580), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        return qimg_isomorph

    def print_isomorphic_graph(self, qimg):
        self.lb_IsomorphicGraphImage.setPixmap(qimg)
    # endregion

    # region Работа с кнопками
    # Возвращаем кнопкам активное состояние
    def enable_buttons(self):
        # Возвращаем кнопкам активное состояние
        self.pb_Cycle.setEnabled(True)
        self.pb_VertexRatio.setEnabled(True)

    # Блокируем состояние кнопок
    def block_buttons(self):
        # Блокируем кнопки
        self.pb_Cycle.setEnabled(False)
        self.pb_VertexRatio.setEnabled(False)
    # endregion

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # Запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # Запускаем функцию main()
