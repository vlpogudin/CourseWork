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
        self.isomorphic_hamiltonias_cycle = []

        self.start_dialog()

        self.pb_VertexRatio.clicked.connect(self.push_vertex_ratio)  # Нажатие на кнопку "Соотношение сторон"
        self.pb_Cycle.clicked.connect(self.push_cycle)  # Нажатие на кнопку "Гамильтонов цикл"
        self.pb_NewDialog.clicked.connect(self.clear_widgets)  # Нажатие на кнопку "Новый диалог"
        self.pb_Deception.clicked.connect(self.push_deception)  # Нажатие на кнопку "Обмануть"
        self.pb_CorrectGraph.clicked.connect(self.push_correct_graph)  # Нажатие на кнопку "Верный граф"
        self.pb_CheckGraph.clicked.connect(self.push_check_graph)  # Нажатие на кнопку "Проверить граф"

        # Добавляем горячую клавишу для открытия руководства пользователя
        keyboard.add_hotkey("f1", self.open_documentation)

    # Функция обработки выбора доказывающей стороны
    def prover_choice(self):
        # Печатаем сообщение выбора в окно доказывающей стороны
        self.te_DialogWindow_2.append("** Мне нужно сделать выбор: попытаться обмануть собеседника "
                                      "или предоставить верный граф... **")
        self.prover_enabled_buttons()  # Разблокирование кнопок для выбора доказывающей стороны

    # Функция обработки начала диалога
    def start_dialog(self):
        self.block_buttons()  # Блокируем кнопки до момента, пока доказывающая сторона не сделает выбор
        self.prover_choice()  # Печатаем сообщение для выбора действий доказывающей стороны

    def push_deception(self):
        pass

    def push_correct_graph(self):
        self.te_DialogWindow_2.clear()  # Очистка диалогового окна доказывающей стороны
        qimg_orig = self.save_original_graph()  # Создание оригинального корректного графа
        self.print_original_graph(qimg_orig)  # Печать созданного графа
        self.print_messages_after_choice()  # Печать сообщений после выбора доказывающей стороны

    def push_check_graph(self):
        pass

    def print_messages_after_choice(self):
        # Создание списка сообщений, выведенных в окна диалога
        self.messages = [
            "Доказывающий: Я знаю Гамильтонов цикл в исходном графе.",
            "Проверяющий: Докажи, что ты действительно знаешь цикл!",
            "Доказывающий: Я не буду показывать тебе реальный исходный граф. "
            "Докажу тебе это, используя изоморфный ему граф!"
        ]

        self.timer = QtCore.QTimer()  # Создание таймера для печати сообщений
        self.timer.timeout.connect(self.print_next_messages)  # Подключение функции вывода сообщений к таймеру
        self.timer.start(100)  # Запуск таймера на 1,5 сек., имитируя раздумья сторон

        self.message_index = 0  # Сохранение индекса сообщений для печати

    # region Начало диалога
    # Печать следующего сообщения по таймеру
    def print_next_messages(self):
        if self.message_index < len(self.messages) and self.message_index % 2 == 0:
            # Выводим текущее сообщение в текстовое поле проверяющей стороны
            self.te_DialogWindow.append(self.messages[self.message_index])
            # Увеличиваем счетчик, чтобы вывести следующее сообщение
            self.message_index += 1
        elif self.message_index < len(self.messages) and self.message_index % 2 != 0:
            # Выводим текущее сообщение в текстовое поле проверяющей стороны
            self.te_DialogWindow_2.append(self.messages[self.message_index])
            # Увеличиваем счетчик, чтобы вывести следующее сообщение
            self.message_index += 1
        # Если все сообщения выведены
        else:
            self.timer.stop()  # Останавливаем таймер
            self.prover_block_buttons()  # Блокировка кнопок для доказывающей стороны
            self.inspector_enable_buttons()  # Разблокировка кнопок для проверяющей стороны
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
        vertex_ratio = methods.show_compliance_node(self.orig_hamiltonias_cycle, self.isomorphic_hamiltonias_cycle)
        self.te_DialogWindow.append(vertex_ratio)
        # Возвращаем кнопкам активное состояние
        self.inspector_enable_buttons()
    # endregion

    # region Обработка нажатия на кнопку "Гамильтонов цикл"
    # Обработка нажатия на кнопку "Гамильтонов цикл"
    def push_cycle(self):
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
        hamiltonias_cycle = methods.print_hamiltonias_cycle(self.isomorphic_hamiltonias_cycle)
        self.te_DialogWindow.append(hamiltonias_cycle)
        # Возвращаем кнопкам активное состояние
        self.inspector_enable_buttons()

    # endregion

    # region Обработка нажатия на кнопку "Новый диалог"
    # Обработка кнопки "Новый диалог" (очистка всех виджетов)
    def clear_widgets(self):
        self.te_DialogWindow.clear()  # Очистка диалогового окна проверяющей стороны
        self.te_DialogWindow_2.clear()  # Очистка диалогового окна доказывающей стороны
        self.start_dialog()  # Старт нового диалога
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
        graph_original = methods.create_big_graph(7, 15)

        # Запоминаем гамильтонов цикл в исходном графе
        self.orig_hamiltonias_cycle = methods.find_hamiltonias_cycle_original_graph(graph_original)

        # Добавляем ребра в граф
        graph_original = methods.add_random_edges(graph_original, 0.2)
        return graph_original

    # Сохранение исходного графа
    def save_original_graph(self):
        # Создание объекта фигуры и объекта оси
        fig, ax = plt.subplots(figsize=(8, 8))

        # Печать графа для запоминания картинки
        nx.draw(self.graph_original, with_labels=True, node_size=500, node_color='skyblue',
                font_size=12, font_color='black',
                font_weight='bold', edge_color='gray',
                linewidths=1, pos=nx.circular_layout(self.graph_original))

        # Сохраняем файл картинки с графом
        fig.savefig('OriginalGraph.png')
        plt.close(fig)
        # Считываем картинку и запоминаем её как QPixmap
        qimg = QPixmap('OriginalGraph.png')
        qimg = qimg.scaled(QSize(660, 520), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
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
        self.isomorphic_hamiltonias_cycle = methods.find_hamiltonias_cycle_isomorphic_graph(self.orig_hamiltonias_cycle, list)

        # Печать графа для запоминания картинки
        nx.draw(graph_isomorphic, with_labels=True, node_size=500, node_color='coral',
                font_size=12, font_color='black',
                font_weight='bold', edge_color='gray',
                linewidths=1, pos=nx.spring_layout(graph_isomorphic))

        # Сохраняем файл картинки с графом
        fig.savefig('IsomorphicGraph.png')
        plt.close(fig)
        # Считываем картинку и запоминаем её как QPixmap
        qimg_isomorph = QPixmap('IsomorphicGraph.png')
        qimg_isomorph = qimg_isomorph.scaled(QSize(660, 520), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        return qimg_isomorph

    def print_isomorphic_graph(self, qimg):
        self.lb_IsomorphicGraphImage.setPixmap(qimg)
    # endregion

    # region Работа с кнопками
    # Возвращаем кнопкам активное состояние
    def inspector_enable_buttons(self):
        self.pb_Cycle.setEnabled(True)  # Разблокировка кнопки "Гамильтонов цикл"
        self.pb_VertexRatio.setEnabled(True)  # Разблокировка кнопки "Соответствие вершин"
        self.pb_CheckGraph.setEnabled(True)  # Разблокировка кнопки "Проверить граф"

    def prover_enabled_buttons(self):
        self.pb_Deception.setEnabled(True)  # Разблокировка кнопки "Обмануть"
        self.pb_CorrectGraph.setEnabled(True)  # Разблокировка кнопки "Верный граф"

    def prover_block_buttons(self):
        self.pb_Deception.setEnabled(False)  # Блокировка кнопки "Обмануть"
        self.pb_CorrectGraph.setEnabled(False)  # Блокировка кнопки "Верный граф"

    # Блокируем состояние кнопок
    def block_buttons(self):
        # Блокируем кнопки
        self.pb_Cycle.setEnabled(False)
        self.pb_VertexRatio.setEnabled(False)
        self.pb_Deception.setEnabled(False)
        self.pb_CorrectGraph.setEnabled(False)
        self.pb_CheckGraph.setEnabled(False)
    # endregion

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # Запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # Запускаем функцию main()
