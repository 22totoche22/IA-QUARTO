# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import game
import ia
from collections import deque
from random import randrange

launched_game = game.Game(game.SIZE)
PICTURES = True

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



        #tailel du bag
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



        '''Initialisation'''
        #cree le nombre de colonnes et lignes
        self.tableWidget.setRowCount(game.SIZE)
        self.tableWidget.setColumnCount(game.SIZE)
        self.tableWidget.setHorizontalHeaderLabels([str(i) for i in (range(game.SIZE))])
        self.tableWidget.setVerticalHeaderLabels([str(i) for i in (range(game.SIZE))])
        self.tab_disabled = None

        # ajout des items dans le sac
        if game.SIZE ==4 and PICTURES:
            for i in range(len(launched_game.bag)):
                item = QtWidgets.QListWidgetItem()
                item.setText(str(i) + ' : ' + str(launched_game.bag[i].charact))
                font = QtGui.QFont()
                palette=QtGui.QBrush()
                palette.setColor(QtGui.QColor(255,255,255))
                font.setPixelSize(1)
                item.setFont(font)
                item.setForeground(palette)
                text = ''
                for i in launched_game.bag[i].charact:
                    text += str(i)
                icon_path = "../images/" + text + ".png"
                icon = QtGui.QIcon(icon_path)
                item.setIcon(icon)
                self.listWidget.addItem(item)
                self.listWidget.setIconSize(QtCore.QSize(30, 30))
        else :
            self.listWidget.addItems([str(i)+' : '+str(launched_game.bag[i].charact) for i in range(len(launched_game.bag))])
        self.listWidget.addItems([None])  # probleme sinon dans le cas ou la liste est vide
        self.listWidget.item(len(launched_game.bag)).setFlags(QtCore.Qt.ItemIsEnabled)


        self.label_7.setText("Choisis qui commence")
        self.list_disabled(True)
        self.table_disabled(True)
        self.first = True
        launched_game.current_player =None



        ########

        '''connect'''

        self.listWidget.itemSelectionChanged.connect(self.ecrit_piece)
        self.tableWidget.itemSelectionChanged.connect(self.ecrit_coord)
        self.buttonBox.rejected.connect(self.annul)
        self.buttonBox.accepted.connect(self.joue_piece)

        self.pushButton_2.clicked.connect(self.choose)
        self.pushButton_3.clicked.connect(self.chooseb)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        '''les fonctions'''

    def choose(self):
        if self.first:
            self.pushButton_2.setStyleSheet(" font : bold 12px")
            self.pushButton_3.setStyleSheet("")
            launched_game.current_player = 1

    def chooseb(self):
        if self.first:
            self.pushButton_3.setStyleSheet(" font : bold 12px")
            self.pushButton_2.setStyleSheet("")
            launched_game.current_player = -1

    def change_time(self):
        self.time = self.time.addSecs(1)
        self.label_4.setText(self.time.toString("hh:mm:ss"))

    def annul(self):
        pass

    def list_disabled(self,bool):
        if bool :
            self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
            self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        else:
            self.listWidget.setFocusPolicy(True)
            self.listWidget.setSelectionMode(True)

    def table_disabled(self,bool):
        if bool:
            self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
            self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
            self.tab_disabled = True
        else:
            self.tableWidget.setFocusPolicy(True)
            self.tableWidget.setSelectionMode(True)
            self.tab_disabled = False


    def first_play(self): #traite le premier cas
        if launched_game.current_player == 1:
            self.list_disabled(False)
            self.table_disabled(True)
            self.label_7.setText("Choisis une pièce")
            if self.listWidget.selectedItems():
                self.list_disabled(True)
                self.table_disabled(True)
                launched_game.select_piece(int(self.listWidget.currentItem().text()[0:2]))
                launched_game.turns_played = deque([(None, launched_game.selected_piece.num)])
                self.pushButton_3.setStyleSheet(" font : bold 12px")
                self.pushButton_2.setStyleSheet("")
                self.first = False
                launched_game.current_player = -1
                self.label_7.setText("laisse moi réfléchir !")
        else:
            self.list_disabled(False)
            self.table_disabled(False)
            num_piece = randrange(0, ((game.SIZE) ** 2) - 1)
            launched_game.select_piece(num_piece)
            item = self.listWidget.findItems(str(num_piece) + ' :', QtCore.Qt.MatchStartsWith)[0]
            self.listWidget.setCurrentItem(item)
            launched_game.turns_played = deque([(None, launched_game.selected_piece.num)])
            self.first = False
            self.pushButton_2.setStyleSheet(" font : bold 12px")
            self.pushButton_3.setStyleSheet("")
            launched_game.current_player = 1
            self.label_7.setText("Place la pièce")
            self.list_disabled(True)


    def joue_piece(self):
        if self.first:
            self.first_play()
        else: #durant la partie

            if launched_game.current_player == 1: #tour du joueur
                if not self.tab_disabled:
                   row = self.tableWidget.currentRow()
                   col = self.tableWidget.currentColumn()
                   if self.lineEdit.text()!='':
                    launched_game.coord = (row,col)
                    if self.tableWidget.item(row, col) == None:
                        self.list_disabled(True)
                        self.table_disabled(False)
                        if game.SIZE == 4 and PICTURES:
                            item = QtWidgets.QTableWidgetItem()
                            text = ''
                            for i in launched_game.selected_piece.charact:
                                text += str(i)
                            icon_path = "../images/" + text + ".png"
                            icon = QtGui.QIcon(icon_path)
                            item.setIcon(icon)
                            #item.setSizeHint(QtCore.QSize(300,300))
                            #item.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                            self.tableWidget.setIconSize(QtCore.QSize(60, 60))
                        else:
                            item = QtWidgets.QTableWidgetItem(self.listWidget.currentItem().text())

                        self.tableWidget.setItem(row, col, item)
                        self.tableWidget.item(row, col).setFlags(QtCore.Qt.ItemIsEnabled)
                        launched_game.play_piece((row, col))
                        launched_game.win = launched_game.full_row((row,col), launched_game.size) #launched_game.full_row2((row,col))
                        launched_game.end = launched_game.win
                        self.listWidget.takeItem(self.listWidget.currentRow())
                        self.list_disabled(False)
                        self.table_disabled(True)
                        self.listWidget.clearSelection()
                        self.tableWidget.clearSelection()
                        self.lineEdit.clear()
                        self.lineEdit_2.clear()
                        if launched_game.end:
                            self.pushButton.setStyleSheet("color : red; font : bold 16px")
                            self.tableWidget.setDisabled(True)
                            self.listWidget.setDisabled(True)
                        self.label_7.setText("Choisis une pièce")
                else:
                    if self.listWidget.selectedItems():
                        num = int(self.listWidget.currentItem().text()[0:2]) # à generaliser
                        launched_game.select_piece(num)
                        launched_game.turns_played.append((launched_game.coord, num))
                        print(launched_game.turns_played)
                        self.list_disabled(True)
                        self.table_disabled(True)
                        launched_game.current_player = -1
                        self.pushButton_3.setStyleSheet(" font : bold 12px")
                        self.pushButton_2.setStyleSheet("")
                        self.label_7.setText("laisse moi réfléchir !")

            else:   #tour du joueur
                    rappel = launched_game.selected_piece.charact
                    self.list_disabled(False)
                    if len(launched_game.bag) == launched_game.size**2 - 1:
                        num = randrange(launched_game.size**2 - 1)
                        while num == launched_game.selected_piece:
                            num = randrange(launched_game.size**2 - 1)
                        (coordinates, num_piece) = ((randrange(launched_game.size), randrange(launched_game.size)), num)

                    # ((coordinates, num_piece), v) = ia.minimax(launched_game, 3)
                    #((coordinates, num_piece), v) = ia.alphabeta(launched_game, 3)
                    elif len(launched_game.bag) >= 2**launched_game.size - launched_game.size:
                        ((coordinates, num_piece), v) = ia.alphabeta(launched_game, 2)
                    elif 2**launched_game.size - launched_game.size > len(launched_game.bag) >= 6 :#2*launched_game.size :
                        ((coordinates, num_piece), v) = ia.alphabeta(launched_game, 3)
                    else :# len(launched_game.bag) <= launched_game.size :
                        ((coordinates, num_piece), v) = ia.alphabeta(launched_game, 6)

                    launched_game.play_turn(coordinates, num_piece)
                    row = coordinates[0]
                    col = coordinates[1]
                    if game.SIZE == 4 and PICTURES:
                        item = QtWidgets.QTableWidgetItem()
                        text = ''
                        for i in rappel:
                            text += str(i)
                        icon_path = "../images/" + text + ".png"
                        icon = QtGui.QIcon(icon_path)
                        item.setIcon(icon)
                        self.tableWidget.setIconSize(QtCore.QSize(100, 100))
                    else:
                        item = QtWidgets.QTableWidgetItem(self.listWidget.currentItem().text())
                    self.tableWidget.setItem(row, col, item)


                    self.listWidget.takeItem(self.listWidget.currentRow())
                    self.tableWidget.item(row, col).setFlags(QtCore.Qt.ItemIsEnabled)
                    if not num_piece == None:
                        item = self.listWidget.findItems(str(num_piece)+' :',QtCore.Qt.MatchStartsWith)[0] #return a list of the item which have the beginning asked
                        self.listWidget.setCurrentItem(item)

                    print(launched_game.turns_played)
                    print(launched_game.board)
                    print(launched_game)
                    self.table_disabled(False)
                    self.list_disabled(True)
                    launched_game.current_player = 1
                    self.pushButton_2.setStyleSheet(" font : bold 12px")
                    self.pushButton_3.setStyleSheet("")
                    self.label_7.setText("Place la pièce")

                    if launched_game.end:
                        self.pushButton.setStyleSheet("color : red; font : bold 16px")
                        self.tableWidget.setDisabled(True)
                        self.listWidget.setDisabled(True)
                        print(launched_game)
                        print(launched_game.turns_played)

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

