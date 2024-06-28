# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1390, 907)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_MultTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_MultTabs.setGeometry(QtCore.QRect(0, 0, 1391, 901))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab_MultTabs.setFont(font)
        self.tab_MultTabs.setObjectName("tab_MultTabs")
        self.tb_info = QtWidgets.QWidget()
        self.tb_info.setObjectName("tb_info")
        self.lb_HiPicture = QtWidgets.QLabel(self.tb_info)
        self.lb_HiPicture.setGeometry(QtCore.QRect(10, 50, 491, 801))
        self.lb_HiPicture.setText("")
        self.lb_HiPicture.setPixmap(QtGui.QPixmap("C:\\Users\\pogud\\Downloads\\Криптография.jpg"))
        self.lb_HiPicture.setScaledContents(True)
        self.lb_HiPicture.setObjectName("lb_HiPicture")
        self.lb_Title = QtWidgets.QLabel(self.tb_info)
        self.lb_Title.setGeometry(QtCore.QRect(10, 10, 341, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Title.setFont(font)
        self.lb_Title.setObjectName("lb_Title")
        self.layoutWidget = QtWidgets.QWidget(self.tb_info)
        self.layoutWidget.setGeometry(QtCore.QRect(520, 90, 851, 721))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vlt_InfoText = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vlt_InfoText.setContentsMargins(0, 0, 0, 0)
        self.vlt_InfoText.setObjectName("vlt_InfoText")
        self.lb_text1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_text1.setFont(font)
        self.lb_text1.setWordWrap(True)
        self.lb_text1.setObjectName("lb_text1")
        self.vlt_InfoText.addWidget(self.lb_text1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vlt_InfoText.addItem(spacerItem)
        self.lv_text2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lv_text2.setFont(font)
        self.lv_text2.setWordWrap(True)
        self.lv_text2.setObjectName("lv_text2")
        self.vlt_InfoText.addWidget(self.lv_text2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vlt_InfoText.addItem(spacerItem1)
        self.lv_text3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lv_text3.setFont(font)
        self.lv_text3.setWordWrap(True)
        self.lv_text3.setObjectName("lv_text3")
        self.vlt_InfoText.addWidget(self.lv_text3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vlt_InfoText.addItem(spacerItem2)
        self.lb_text4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_text4.setFont(font)
        self.lb_text4.setWordWrap(True)
        self.lb_text4.setObjectName("lb_text4")
        self.vlt_InfoText.addWidget(self.lb_text4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vlt_InfoText.addItem(spacerItem3)
        self.lb_text5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_text5.setFont(font)
        self.lb_text5.setWordWrap(True)
        self.lb_text5.setObjectName("lb_text5")
        self.vlt_InfoText.addWidget(self.lb_text5)
        self.tab_MultTabs.addTab(self.tb_info, "")
        self.tb_program = QtWidgets.QWidget()
        self.tb_program.setObjectName("tb_program")
        self.te_DialogWindow = QtWidgets.QTextEdit(self.tb_program)
        self.te_DialogWindow.setGeometry(QtCore.QRect(10, 80, 411, 711))
        self.te_DialogWindow.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.te_DialogWindow.setFont(font)
        self.te_DialogWindow.setAcceptDrops(True)
        self.te_DialogWindow.setStyleSheet("border: 1px solid black;")
        self.te_DialogWindow.setObjectName("te_DialogWindow")
        self.lb_OrigGraphImage = QtWidgets.QLabel(self.tb_program)
        self.lb_OrigGraphImage.setGeometry(QtCore.QRect(440, 50, 501, 371))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_OrigGraphImage.setFont(font)
        self.lb_OrigGraphImage.setText("")
        self.lb_OrigGraphImage.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_OrigGraphImage.setObjectName("lb_OrigGraphImage")
        self.lb_Title_2 = QtWidgets.QLabel(self.tb_program)
        self.lb_Title_2.setGeometry(QtCore.QRect(530, 10, 331, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Title_2.setFont(font)
        self.lb_Title_2.setObjectName("lb_Title_2")
        self.lb_IsomorphicGraphImage = QtWidgets.QLabel(self.tb_program)
        self.lb_IsomorphicGraphImage.setGeometry(QtCore.QRect(440, 420, 501, 371))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_IsomorphicGraphImage.setFont(font)
        self.lb_IsomorphicGraphImage.setText("")
        self.lb_IsomorphicGraphImage.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_IsomorphicGraphImage.setObjectName("lb_IsomorphicGraphImage")
        self.te_DialogWindow_2 = QtWidgets.QTextEdit(self.tb_program)
        self.te_DialogWindow_2.setGeometry(QtCore.QRect(960, 80, 411, 711))
        self.te_DialogWindow_2.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.te_DialogWindow_2.setFont(font)
        self.te_DialogWindow_2.setAcceptDrops(True)
        self.te_DialogWindow_2.setStyleSheet("border: 1px solid black;")
        self.te_DialogWindow_2.setObjectName("te_DialogWindow_2")
        self.lb_DeceptionProbability = QtWidgets.QLabel(self.tb_program)
        self.lb_DeceptionProbability.setGeometry(QtCore.QRect(600, 820, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_DeceptionProbability.setFont(font)
        self.lb_DeceptionProbability.setObjectName("lb_DeceptionProbability")
        self.lb_Percentage = QtWidgets.QLabel(self.tb_program)
        self.lb_Percentage.setGeometry(QtCore.QRect(810, 820, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_Percentage.setFont(font)
        self.lb_Percentage.setObjectName("lb_Percentage")
        self.layoutWidget1 = QtWidgets.QWidget(self.tb_program)
        self.layoutWidget1.setGeometry(QtCore.QRect(1120, 820, 251, 35))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pb_CorrectGraph = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_CorrectGraph.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_CorrectGraph.sizePolicy().hasHeightForWidth())
        self.pb_CorrectGraph.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_CorrectGraph.setFont(font)
        self.pb_CorrectGraph.setObjectName("pb_CorrectGraph")
        self.horizontalLayout_3.addWidget(self.pb_CorrectGraph)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pb_Deception = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_Deception.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Deception.sizePolicy().hasHeightForWidth())
        self.pb_Deception.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_Deception.setFont(font)
        self.pb_Deception.setObjectName("pb_Deception")
        self.horizontalLayout_3.addWidget(self.pb_Deception)
        self.lb_Title_3 = QtWidgets.QLabel(self.tb_program)
        self.lb_Title_3.setGeometry(QtCore.QRect(10, 50, 411, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Title_3.setFont(font)
        self.lb_Title_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_Title_3.setObjectName("lb_Title_3")
        self.lb_Title_4 = QtWidgets.QLabel(self.tb_program)
        self.lb_Title_4.setGeometry(QtCore.QRect(960, 50, 411, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Title_4.setFont(font)
        self.lb_Title_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_Title_4.setObjectName("lb_Title_4")
        self.pb_NewDialog = QtWidgets.QPushButton(self.tb_program)
        self.pb_NewDialog.setGeometry(QtCore.QRect(1230, 10, 138, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_NewDialog.sizePolicy().hasHeightForWidth())
        self.pb_NewDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pb_NewDialog.setFont(font)
        self.pb_NewDialog.setObjectName("pb_NewDialog")
        self.widget = QtWidgets.QWidget(self.tb_program)
        self.widget.setGeometry(QtCore.QRect(12, 820, 572, 35))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_VertexRatio = QtWidgets.QPushButton(self.widget)
        self.pb_VertexRatio.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_VertexRatio.sizePolicy().hasHeightForWidth())
        self.pb_VertexRatio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_VertexRatio.setFont(font)
        self.pb_VertexRatio.setObjectName("pb_VertexRatio")
        self.horizontalLayout.addWidget(self.pb_VertexRatio)
        spacerItem5 = QtWidgets.QSpacerItem(13, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pb_Cycle = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Cycle.sizePolicy().hasHeightForWidth())
        self.pb_Cycle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_Cycle.setFont(font)
        self.pb_Cycle.setObjectName("pb_Cycle")
        self.horizontalLayout.addWidget(self.pb_Cycle)
        spacerItem6 = QtWidgets.QSpacerItem(13, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pb_CheckGraph = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_CheckGraph.sizePolicy().hasHeightForWidth())
        self.pb_CheckGraph.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_CheckGraph.setFont(font)
        self.pb_CheckGraph.setObjectName("pb_CheckGraph")
        self.horizontalLayout.addWidget(self.pb_CheckGraph)
        self.tab_MultTabs.addTab(self.tb_program, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_MultTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Криптографический протокол"))
        self.lb_Title.setText(_translate("MainWindow", "Информация о программе"))
        self.lb_text1.setText(_translate("MainWindow", "Программа является вспомогательным элементом в демонстрации работы криптографического протокола доказателльства без раскрытия секрета."))
        self.lv_text2.setText(_translate("MainWindow", "Криптографический протокол с нулевым разглашением позволяет одной стороне (доказывающей) убедить другую сторону (проверяющую) в истинности определённого утверждения, не раскрывая никакой другой информации, кроме самого факта истинности утверждения."))
        self.lv_text3.setText(_translate("MainWindow", "Работа протокола в программе демонстрируется с помощью алгортитма, основанного на доказательстве наличия гамильтонова цикла в исходном графе. Впервые данный пример работы протокола был придуман и представлен публике Мануэлем Блюмом в 1986 году."))
        self.lb_text4.setText(_translate("MainWindow", "Доказывающая сторона уверяет проверяющую в том, что знает гамильтонов цикл в оригинальном графе и хочет это доказать, не раскрывая его. Проверяющая сторона запрашивает различные доказательства и проверяет их. При различных запросах результат может быть отличным, тем самым взаимодействие пользователя с программой принимает некий игровой характер."))
        self.lb_text5.setText(_translate("MainWindow", "Интерфейс программы представлен различными кнопками, окнами демонстрации изображений и полями диалогов, каждые из которых имеют определенный функционал. Перед началом работы рекомендуется ознакомиться с руководством пользователя, в котором описан этап взаимодействия с программой (справку можно открыть горячей клавишей F1)."))
        self.tab_MultTabs.setTabText(self.tab_MultTabs.indexOf(self.tb_info), _translate("MainWindow", "О программе"))
        self.lb_Title_2.setText(_translate("MainWindow", "Демонстрация протокола"))
        self.lb_DeceptionProbability.setText(_translate("MainWindow", "Вероятность обмана:"))
        self.lb_Percentage.setText(_translate("MainWindow", "0"))
        self.pb_CorrectGraph.setText(_translate("MainWindow", "Верный граф"))
        self.pb_Deception.setText(_translate("MainWindow", "Обмануть"))
        self.lb_Title_3.setText(_translate("MainWindow", "Проверяющая сторона"))
        self.lb_Title_4.setText(_translate("MainWindow", "Доказывающая сторона"))
        self.pb_NewDialog.setText(_translate("MainWindow", "Новый диалог"))
        self.pb_VertexRatio.setText(_translate("MainWindow", "Соответствие вершин"))
        self.pb_Cycle.setText(_translate("MainWindow", "Гамильтонов цикл"))
        self.pb_CheckGraph.setText(_translate("MainWindow", "Проверить граф"))
        self.tab_MultTabs.setTabText(self.tab_MultTabs.indexOf(self.tb_program), _translate("MainWindow", "Демонстрация протокола"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
