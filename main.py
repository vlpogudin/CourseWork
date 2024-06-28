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
        super().__init__()
        self.setupUi(self)  # Инициализация дизайна

        self.timer = QtCore.QTimer()  # Создание таймера для печати сообщений

        self.orig_hamiltonias_cycle = []  # Гамильтонов цикл исходного графа

        self.isomorphic_hamiltonias_cycle = []  # Гамильтонов цикл изоморфного графа

        self.deception_percentage = 0  # Вероятность обмана в частях (по умолчанию - 0)
        self.lb_Percentage.setText(str(self.deception_percentage))  # Показываем вероятность обмана в поле вероятности
        self.is_deception = False  # Запоминаем, созданный граф верный или нет (по умолчанию - нет)
        self.action = 0  # Хранение действия (соответствие - 1, цикл - 2)

        self.start_dialog()  # Начало диалога

        # Подключаем нажатие кнопок к определенным функциям
        self.pb_VertexRatio.clicked.connect(self.push_vertex_ratio)  # Нажатие на кнопку "Соотношение сторон"
        self.pb_Cycle.clicked.connect(self.push_cycle)  # Нажатие на кнопку "Гамильтонов цикл"
        self.pb_NewDialog.clicked.connect(self.push_new_dialog)  # Нажатие на кнопку "Новый диалог"
        self.pb_Deception.clicked.connect(self.push_deception)  # Нажатие на кнопку "Обмануть"
        self.pb_CorrectGraph.clicked.connect(self.push_correct_graph)  # Нажатие на кнопку "Верный граф"
        self.pb_CheckGraph.clicked.connect(self.push_check_graph)  # Нажатие на кнопку "Проверить граф"

        # Добавляем горячую клавишу для открытия руководства пользователя
        keyboard.add_hotkey("f1", self.open_documentation)

    # region Работа с вероятностью обмана
    # Функция обновления вероятности обмана
    def update_deception_percentage(self):
        if self.deception_percentage == 0:
            self.deception_percentage = 0.5
        else:
            self.deception_percentage *= 0.5

    # Функция проверки вероятности обмана на достаточность процента
    def check_deception_percentage(self):
        is_full = (self.deception_percentage == 2**(-10))  # Определяем, достигла ли вероятность граничного значения
        if is_full:  # Если достигла
            (self.te_DialogWindow_2.append
             ("Проверяющий: Ты действительно доказал мне, что знаешь гамильтонов цикл в исходном графе."))
            self.block_buttons()  # Блокируем все кнопки, имитируя конец диалога
        else:
            pass
    # endregion

    # region Обработка нажатия на кнопку "Обмануть"
    def push_deception(self):
        self.prover_block_buttons()  # Блокируем кнопки для доказывающей стороны
        self.te_DialogWindow_2.clear()  # Очистка диалогового окна доказывающей стороны
        self.graph_original = methods.create_false_graph(7, 12)  # Создание неверного графа
        self.graph_original = methods.add_random_edges(self.graph_original, 0.2)  # Добавляем ребра
        self.is_deception = True  # Сохраняем, что был создан неверный граф
        orig_qimage = self.save_original_graph()  # Сохранение оригинального неверного графа
        self.print_original_graph(orig_qimage)  # Печать созданного неверного графа
        self.print_messages_after_choice()  # Печать сообщений после выбора доказывающей стороны
    # endregion

    # region Обработка нажатия на кнопку "Верный граф"
    def push_correct_graph(self):
        self.prover_block_buttons()  # Блокируем кнопки для доказывающей стороны
        self.te_DialogWindow_2.clear()  # Очистка диалогового окна доказывающей стороны
        self.graph_original = methods.create_big_graph(7, 12)  # Создание верного графа
        self.orig_hamiltonias_cycle = (
            methods.find_hamiltonias_cycle_original_graph(self.graph_original))  # Сохраняем гамильтонов цикл
        self.graph_original = methods.add_random_edges(self.graph_original, 0.2)  # Добавляем ребра
        self.is_deception = False  # Сохраняем, что был создан верный граф
        # Создание изоморфного графа и сохранение его гамильтонова цикла
        self.graph_isomorphic, self.isomorphic_hamiltonias_cycle = (
            methods.create_isomorphic_graph(self.graph_original))
        qimg_orig = self.save_original_graph()  # Сохранение оригинального верного графа
        self.print_original_graph(qimg_orig)  # Печать созданного верного графа
        self.print_messages_after_choice()  # Печать сообщений после выбора доказывающей стороны
    # endregion

    # region Обработка нажатия на кнопку "Проверить граф"
    def push_check_graph(self):
        if self.action == 1:  # Когда проверка соответствие вершин
            is_compare = methods.compare_graphs(self.graph_original, self.graph_isomorphic)  # Проверяю
            if is_compare:
                self.te_DialogWindow_2.append("Проверяющий: Ты действительно доказал соответствие двух графов.")
                self.inspector_enable_buttons()  # Разблокировка кнопок проверяющей стороны
            else:
                self.te_DialogWindow_2.append("Проверяющий: Вершины твоих графов не соответствуют! Я обнаружил обман.")
                self.block_buttons()  # Блокируем кнопки
        elif self.action == 2:  # Когда проверка гамильтонова цикла
            is_cycle = methods.check_hamiltonias_cycle(self.isomorphic_hamiltonias_cycle, self.graph_isomorphic)
            if is_cycle:
                self.te_DialogWindow_2.append("Проверяющий: Твой гамильтонов цикл верный.")
                self.inspector_enable_buttons()  # Разблокировка кнопок проверяющей стороны
            else:
                self.te_DialogWindow_2.append("Проверяющий: Твой гамильтонов цикл неверный.")
                self.block_buttons()  # Блокируем кнопки
        else:
            self.inspector_enable_buttons()  # Разблокировка кнопок проверяющей стороны
        self.pb_CheckGraph.setEnabled(False)
    # endregion

    # region Начало диалога
    # Функция обработки начала диалога
    def start_dialog(self):
        self.block_buttons()  # Блокируем кнопки до момента, пока доказывающая сторона не сделает выбор
        self.prover_choice()  # Печатаем сообщение для выбора действий доказывающей стороны

    # Функция обработки выбора доказывающей стороны
    def prover_choice(self):
        # Печатаем сообщение выбора в окно доказывающей стороны
        self.te_DialogWindow_2.append("** Мне нужно сделать выбор: попытаться обмануть собеседника "
                                      "или предоставить верный граф... **")
        self.prover_enabled_buttons()  # Разблокирование кнопок для выбора доказывающей стороны
        self.pb_CheckGraph.setEnabled(False)

    # Функция печати сообщений после выбора доказывающей стороны
    def print_messages_after_choice(self):
        # Создание списка сообщений, выведенных в окна диалога
        self.messages = [
            "Доказывающий: Я знаю гамильтонов цикл в исходном графе.",
            "Проверяющий: Докажи, что ты действительно знаешь цикл!",
            "Доказывающий: Я не буду показывать тебе реальный исходный граф. "
            "Докажу тебе это, используя изоморфный ему граф!"
        ]

        self.timer = QtCore.QTimer()  # Создание таймера для печати сообщений
        self.timer.timeout.connect(self.print_next_messages)  # Подключение функции вывода сообщений к таймеру
        self.timer.start(1000)  # Запуск таймера на 1 сек., имитируя раздумья сторон

        self.message_index = 0  # Сохранение индекса сообщений для печати

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
            self.pb_CheckGraph.setEnabled(False)
    # endregion

    # region Обработка нажатия на кнопку "Соответствие вершин"
    # Обработка нажатия на кнопку "Соответствие вершин"
    def push_vertex_ratio(self):
        self.timer.stop()  # Останавливаем таймер
        self.block_buttons()  # Блокируем кнопки
        self.print_question_vertex_ratio()  # Печать запроса проверяющего
        self.action = 1  # Обновляем значение действия

        # Создаем и печатаем изоморфный граф
        qimage_isomorph = self.create_and_save_isomorphic_graph()
        self.print_isomorphic_graph(qimage_isomorph)

        # Спим, изображая раздумья доказывающего
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.print_answer_vertex_ratio)  # Подключаем к нужному слоту
        self.timer.timeout.connect(self.check_deception_percentage)
        self.timer.setSingleShot(True)  # Выполнить только один раз
        self.timer.start(1000)

        self.update_deception_percentage()  # Обновляем вероятность обмана
        self.lb_Percentage.setText(str(self.deception_percentage))  # Показываем вероятность обмана в поле вероятности

    # Печать вопроса проверяющего
    def print_question_vertex_ratio(self):
        # Печать запроса проверяющего
        self.te_DialogWindow_2.append("Проверяющий: Покажи соответствие вершин.")

    # Печать ответа доказывающего
    def print_answer_vertex_ratio(self):
        # Печать ответа доказывающего
        self.te_DialogWindow.append("Доказывающий: Демонстрирую соответствие вершин на графе: ")
        # Печать соответствия вершин
        orig_cycle = self.orig_hamiltonias_cycle.copy()
        isor_cycle = self.isomorphic_hamiltonias_cycle.copy()
        vertex_ratio = methods.show_compliance_node(orig_cycle, isor_cycle)
        self.te_DialogWindow.append(vertex_ratio)
        # Возвращаем кнопкам активное состояние
        self.pb_CheckGraph.setEnabled(True)
    # endregion

    # region Обработка нажатия на кнопку "Гамильтонов цикл"
    # Обработка нажатия на кнопку "Гамильтонов цикл"
    def push_cycle(self):
        self.timer.stop()  # Останавливаем таймер
        self.block_buttons()  # Блокируем кнопки
        self.print_question_cycle()  # Печать запроса проверяющего
        self.action = 2  # Обновляем значение действия

        # Создаем и печатаем изоморфный граф
        qimage_isomorph = self.create_and_save_isomorphic_graph()
        self.print_isomorphic_graph(qimage_isomorph)

        # Спим, изображая раздумья доказывающего
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.print_answer_cycle)  # Подключаем к нужному слоту
        self.timer.timeout.connect(self.check_deception_percentage)
        self.timer.setSingleShot(True)  # Выполнить только один раз
        self.timer.start(1000)

        self.update_deception_percentage()  # Обновляем вероятность обмана
        self.lb_Percentage.setText(str(self.deception_percentage))  # Показываем вероятность обмана в поле вероятности

    # Печать вопроса проверяющего
    def print_question_cycle(self):
        # Печать запроса проверяющего и ответа доказывающего
        self.te_DialogWindow_2.append("Проверяющий: Покажи гамильтонов цикл.")

    # Печать ответа доказывающего
    def print_answer_cycle(self):
        # Печать ответа доказывающего
        self.te_DialogWindow.append("Доказывающий: Показываю гамильтонов цикл в изоморфном графе:")
        # Печать гамильтонова графа
        hamiltonias_cycle = methods.print_hamiltonias_cycle(self.isomorphic_hamiltonias_cycle)
        self.te_DialogWindow.append(hamiltonias_cycle)
        # Возвращаем кнопкам активное состояние
        self.pb_CheckGraph.setEnabled(True)
    # endregion

    # region Обработка нажатия на кнопку "Новый диалог"
    # Обработка кнопки "Новый диалог" (очистка всех виджетов)
    def push_new_dialog(self):
        self.timer.stop()  # Останавливаем таймер
        self.te_DialogWindow.clear()  # Очистка диалогового окна проверяющей стороны
        self.te_DialogWindow_2.clear()  # Очистка диалогового окна доказывающей стороны
        self.lb_IsomorphicGraphImage.clear()  # Очистка окна демонстрации изоморфного графа
        self.lb_OrigGraphImage.clear()  # Очистка окна демонстрации оригинального графа
        self.deception_percentage = 0  # Обнуление вероятности обмана
        self.lb_Percentage.setText(str(self.deception_percentage))  # Печатаем новый
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
        graph_original = methods.create_big_graph(7, 15)  # Создание нового (исходного графа)

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
    def create_and_save_isomorphic_graph(self):
        # Создание объекта фигуры и объекта оси
        fig, ax = plt.subplots(figsize=(8, 8))

        # Создаем изоморфный граф
        if self.is_deception:
            # Создание изоморфного графа и сохранение его гамильтонова цикла
            self.graph_isomorphic, self.isomorphic_hamiltonias_cycle = (
                methods.create_isomorphic_false_graph(self.graph_original))
        else:
            self.graph_isomorphic, list = methods.create_isomorphic_graph(self.graph_original)
            self.isomorphic_hamiltonias_cycle = methods.find_hamiltonias_cycle_isomorphic_graph(self.orig_hamiltonias_cycle, list)

        # Печать графа для запоминания картинки
        nx.draw(self.graph_isomorphic, with_labels=True, node_size=500, node_color='coral',
                font_size=12, font_color='black',
                font_weight='bold', edge_color='gray',
                linewidths=1, pos=nx.spring_layout(self.graph_isomorphic))

        # Сохраняем файл картинки с графом
        fig.savefig('IsomorphicGraph.png')
        plt.close(fig)
        # Считываем картинку и запоминаем её как QPixmap
        qimage_isomorph = QPixmap('IsomorphicGraph.png')
        qimage_isomorph = qimage_isomorph.scaled(QSize(660, 520), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        return qimage_isomorph

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
