# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from collections import deque
from random import randrange
import ui_window
import ia
import game

PICTURES = True
launched_game = game.Game(game.SIZE)


class Ui_interact(ui_window.Ui_MainWindow):

    def __init__(self,MainWindow): #on récupère la fenêtre vide
        super().setupUi(MainWindow)

    def setupUibis(self,MainWindow):

        #ajout des lignes et des colonnes dans le tableau
        self.tableWidget.setRowCount(game.SIZE)
        self.tableWidget.setColumnCount(game.SIZE)
        #renommage du nom des lignes et colonne
        self.tableWidget.setHorizontalHeaderLabels([str(i) for i in (range(game.SIZE))])
        self.tableWidget.setVerticalHeaderLabels([str(i) for i in (range(game.SIZE))])
        self.tab_disabled = None #si le tableau est désactivé

        # ajout des items dans le sac
        if game.SIZE ==4 and PICTURES: # on ajoute les images correspondant aux pièces
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
        else : #sinon on ajoute les listes [,,,] qui correspondent aux images
            self.listWidget.addItems([str(i)+' : '+str(launched_game.bag[i].charact) for i in range(len(launched_game.bag))])
        self.listWidget.addItems([None])  # probleme sinon dans le cas ou la liste est vide
        self.listWidget.item(len(launched_game.bag)).setFlags(QtCore.Qt.ItemIsEnabled)


        self.label_7.setText("Choisis qui commence")
        self.list_disabled(True)
        self.table_disabled(True)
        self.first = True
        launched_game.current_player =None

        '''Temps'''
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.players.addWidget(self.label_4)

        self.time = QtCore.QTime(0, 0, 0)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.change_time)
        self.timer.start(1000)

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

    def choose(self): #si le joueur A est choisi
        if self.first: #cas de l'avant premier tour
            self.pushButton_2.setStyleSheet(" font : bold 12px")
            self.pushButton_3.setStyleSheet("")
            launched_game.current_player = 1

    def chooseb(self): #si le joueur B est choisi (=IA)
        if self.first: #cas de l'avant premier tour
            self.pushButton_3.setStyleSheet(" font : bold 12px")
            self.pushButton_2.setStyleSheet("")
            launched_game.current_player = -1

    def change_time(self):
        self.time = self.time.addSecs(1)
        self.label_4.setText(self.time.toString("hh:mm:ss"))

    def annul(self):
        pass

    def list_disabled(self,bool): #active ou désactive la liste des pièces
        if bool :
            self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
            self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        else:
            self.listWidget.setFocusPolicy(True)
            self.listWidget.setSelectionMode(True)

    def table_disabled(self,bool):#active ou désactive le tableau (board)
        if bool:
            self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
            self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
            self.tab_disabled = True
        else:
            self.tableWidget.setFocusPolicy(True)
            self.tableWidget.setSelectionMode(True)
            self.tab_disabled = False


    def ecrit_piece(self):
        self.lineEdit_2.setText((self.listWidget.currentItem().text()))

    def ecrit_coord(self):
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        self.lineEdit.setText('(' + str(row) + ', ' + str(col) + ')')

    def first_play(self):  # traite le premier cas
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
                self.label_7.setText("Laisse-moi réfléchir! ok ?")
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
        else:  # durant la partie

            if launched_game.current_player == 1:  # tour du joueur
                if not self.tab_disabled:
                    row = self.tableWidget.currentRow()
                    col = self.tableWidget.currentColumn()
                    if self.lineEdit.text() != '':
                        launched_game.coord = (row, col)
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
                                # item.setSizeHint(QtCore.QSize(300,300))
                                # item.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                                self.tableWidget.setIconSize(QtCore.QSize(60, 60))
                            else:
                                item = QtWidgets.QTableWidgetItem(self.listWidget.currentItem().text())

                            self.tableWidget.setItem(row, col, item)
                            self.tableWidget.item(row, col).setFlags(QtCore.Qt.ItemIsEnabled)
                            launched_game.play_piece((row, col))
                            launched_game.win = launched_game.full_row2((row,col)) #launched_game.full_row((row, col),
                                                                       #launched_game.size)
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
                        num = int(self.listWidget.currentItem().text()[0:2])  # à generaliser
                        launched_game.select_piece(num)
                        launched_game.turns_played.append((launched_game.coord, num))
                        print(launched_game.turns_played)
                        self.list_disabled(True)
                        self.table_disabled(True)
                        launched_game.current_player = -1
                        self.pushButton_3.setStyleSheet(" font : bold 12px")
                        self.pushButton_2.setStyleSheet("")
                        self.label_7.setText("Laisse-moi réfléchir! ok ?")

            else:  # tour du joueur
                rappel = launched_game.selected_piece.charact
                self.list_disabled(False)
                (coordinates, num_piece) = ia.select_best_turn(launched_game)

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
                    item = self.listWidget.findItems(str(num_piece) + ' :', QtCore.Qt.MatchStartsWith)[
                        0]  # return a list of the item which have the beginning asked
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
