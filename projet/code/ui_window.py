# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setMinimumSize(800, 720)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Principale = QtWidgets.QVBoxLayout()
        self.Principale.setContentsMargins(-1, 0, -1, 0)
        self.Principale.setSpacing(6)
        self.Principale.setObjectName("Principale")
        ########
        self.title = QtWidgets.QHBoxLayout()
        self.title.setContentsMargins(-1, 0, -1, -1)
        self.title.setSpacing(6)
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.title.addWidget(self.label)
        self.Principale.addLayout(self.title)
        ########
        ########
        self.table_list = QtWidgets.QHBoxLayout()
        self.table_list.setSpacing(6)
        self.table_list.setObjectName("table_list")
        '''board'''
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setObjectName("tableWidget")
        self.table_list.addWidget(self.tableWidget)
        #etire les cellules
        self.stretchLastSection = True
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #caracteristiques headers
        self.tableWidget.setStyleSheet("QHeaderView:section { background-color:grey }")
        #simple selection et non-edition des cellules
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        '''bag'''
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.table_list.addWidget(self.listWidget)
        #taille du bag
        self.listWidget.setMaximumWidth(150)
        self.Principale.addLayout(self.table_list)
        ########
        ########
        self.choice = QtWidgets.QHBoxLayout()
        self.choice.setSpacing(6)
        self.choice.setObjectName("choice")
        '''Piece'''
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.choice.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.choice.addWidget(self.lineEdit_2)
        #lecture et masque
        #self.lineEdit_2.setInputMask(" \[ 0, 0, 0, 0 \] ")
        self.lineEdit_2.setReadOnly(True)
        '''coords'''
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.choice.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.choice.addWidget(self.lineEdit)
        # lecture et masque
        #self.lineEdit.setInputMask(" (0, 0) ")
        self.lineEdit.setReadOnly(True)
        '''play'''
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.choice.addWidget(self.buttonBox)
        self.Principale.addLayout(self.choice)
        ########
        ########
        self.players = QtWidgets.QHBoxLayout()
        self.players.setContentsMargins(-1, -1, -1, 0)
        self.players.setSpacing(6)
        self.players.setObjectName("players")
        '''PlayerA'''
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setObjectName("pushButton")
        self.players.addWidget(self.pushButton_2)
        '''PlayerB'''
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setObjectName("pushButton")
        self.players.addWidget(self.pushButton_3)
        '''Indications'''
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.players.addWidget(self.label_7)
        self.Principale.addLayout(self.players)
        ########
        self.quarto = QtWidgets.QHBoxLayout()
        self.quarto.setContentsMargins(-1, 0, -1, -1)
        self.quarto.setSpacing(6)
        self.quarto.setObjectName("quarto")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.quarto.addWidget(self.pushButton)
        self.Principale.addLayout(self.quarto)
        self.verticalLayout_2.addLayout(self.Principale)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 517, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ########

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jeu de quarto"))
        self.label.setText(_translate("MainWindow", "Jeu de quarto"))
        self.label.setStyleSheet("color: red; font : bold 16px")
        self.tableWidget.setSortingEnabled(False)
        self.label_2.setText(_translate("MainWindow", "Pièce:"))
        self.label_3.setText(_translate("MainWindow", "Coordonéés:"))
        self.pushButton_2.setText(_translate("MainWindow", "Bob"))
        self.pushButton_3.setText(_translate("MainWindow", "Charles-Maurice"))
        self.pushButton.setText(_translate("MainWindow", "\"Quarto\""))
        self.pushButton.setStyleSheet("font : bold 12px")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

