# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


board = [[[None for i in range(4)] for j in range(4)] for k in range(4)]
d={0: [0, 0, 0, 0], 1: [0, 0, 0, 1], 2: [0, 0, 1, 0], 3: [0, 0, 1, 1], 4: [0, 1, 0, 0], 5: [0, 1, 0, 1], 6: [0, 1, 1, 0], 7: [0, 1, 1, 1], 8: [1, 0, 0, 0], 9: [1, 0, 0, 1], 10: [1, 0, 1, 0], 11: [1, 0, 1, 1], 12: [1, 1, 0, 0], 13: [1, 1, 0, 1], 14: [1, 1, 1, 0], 15: [1, 1, 1, 1]}
size = 4



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(517, 363)
        MainWindow.setMinimumSize(600, 455)


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

        #cree le nombre de colonnes et lignes
        self.tableWidget.setRowCount(size)
        self.tableWidget.setColumnCount(size)

        self.tableWidget.setObjectName("tableWidget")
        self.table_list.addWidget(self.tableWidget)

        #etire les cellules
        self.stretchLastSection = True
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        #caracteristiques headers
        self.tableWidget.setStyleSheet("QHeaderView:section { background-color:grey }")
        self.tableWidget.setHorizontalHeaderLabels([str(i) for i in (range(size))])
        self.tableWidget.setVerticalHeaderLabels([str(i) for i in (range(size))])

        #simple selection et non-edition des cellules
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)



        '''bag'''
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.table_list.addWidget(self.listWidget)

        #ajout des items dans le sac
        self.listWidget.addItems([str(d[i]) for i in range(len(d))])
        self.listWidget.addItems([None]) #probleme sinon dans le cas ou la liste est vide

        #tailel du bag
        self.listWidget.setMaximumWidth(100)


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
        self.lineEdit_2.setInputMask(" \[ 0, 0, 0, 0 \] ")
        self.lineEdit_2.setReadOnly(True)


        '''coords'''


        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.choice.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.choice.addWidget(self.lineEdit)

        # lecture et masque
        self.lineEdit.setInputMask(" (0, 0) ")
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
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.players.addWidget(self.label_6)
        self.label_6.setStyleSheet(" font : bold 12px")

        '''PlayerB'''
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.players.addWidget(self.label_5)

        '''Temps'''
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.players.addWidget(self.label_4)


        self.time = QtCore.QTime(0, 0, 0)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.change_time)
        self.timer.start(1000)

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


        ########

        '''connect'''

        self.listWidget.itemSelectionChanged.connect(self.ecrit_piece)
        self.tableWidget.itemSelectionChanged.connect(self.ecrit_coord)
        self.buttonBox.rejected.connect(self.annul)
        self.buttonBox.rejected.connect(self.annul)
        self.buttonBox.accepted.connect(self.joue_piece)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def change_time(self):
        self.time = self.time.addSecs(1)
        self.label_4.setText(self.time.toString("hh:mm:ss"))

    def annul(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.tableWidget.clearSelection()
        self.listWidget.clearSelection()

    def joue_piece(self):

        if self.listWidget.selectedItems(): #si un item selectionné dans le bag(sinon renvoie liste vide = false) et si
            row = self.tableWidget.currentRow()
            col = self.tableWidget.currentColumn()
            if self.tableWidget.item(row, col) == None:  #si la cellule est vide
                item = QtWidgets.QTableWidgetItem(self.listWidget.currentItem().text())
                self.tableWidget.setItem(row, col, item)
                self.tableWidget.item(row, col).setFlags(QtCore.Qt.ItemIsEnabled)
                self.listWidget.takeItem(self.listWidget.currentRow())
                self.listWidget.clearSelection()
                self.tableWidget.clearSelection()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
            long = len(self.listWidget)
            if long %2 ==0:
                self.label_6.setStyleSheet("font : bold 12px")
                self.label_5.setStyleSheet("")
            else :
                self.label_6.setStyleSheet("")
                self.label_5.setStyleSheet("font : bold 12px")


    def ecrit_piece(self):
        self.lineEdit_2.setText((self.listWidget.currentItem().text()))

    def ecrit_coord(self):
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        self.lineEdit.setText('(' + str(row) + ', ' + str(col) + ')')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Jeu de quarto"))
        self.label.setStyleSheet("color: red; font : bold 16px")
        self.tableWidget.setSortingEnabled(False)
        self.label_2.setText(_translate("MainWindow", "Pièce:"))
        self.label_3.setText(_translate("MainWindow", "Coordonéés:"))
        self.label_6.setText(_translate("MainWindow", "Player A"))
        self.label_5.setText(_translate("MainWindow", "Player B"))
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

