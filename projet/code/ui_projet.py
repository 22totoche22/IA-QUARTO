# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
board = [[[None for i in range(4)] for j in range(4)] for k in range(4)]
d={0: [0, 0, 0, 0], 1: [0, 0, 0, 1], 2: [0, 0, 1, 0], 3: [0, 0, 1, 1], 4: [0, 1, 0, 0], 5: [0, 1, 0, 1], 6: [0, 1, 1, 0], 7: [0, 1, 1, 1], 8: [1, 0, 0, 0], 9: [1, 0, 0, 1], 10: [1, 0, 1, 0], 11: [1, 0, 1, 1], 12: [1, 1, 0, 0], 13: [1, 1, 0, 1], 14: [1, 1, 1, 0], 15: [1, 1, 1, 1]}
size = 4

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(517, 363)
        MainWindow.setMinimumSize(600, 425)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")


        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setRowCount(size)
        self.tableWidget.setColumnCount(size)
        self.tableWidget.setObjectName("tableWidget")
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.stretchLastSection = True
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setStyleSheet("QHeaderView:section { background-color:grey }")
        self.tableWidget.setHorizontalHeaderLabels([str(i) for i in (range(size))])
        self.tableWidget.setVerticalHeaderLabels([str(i) for i in (range(size))])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)



        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_3.addWidget(self.listWidget)
        self.listWidget.addItems([str(d[i]) for i in range(len(d))])
        self.listWidget.setMaximumWidth(100)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_2.setInputMask(" \[ 0, 0, 0, 0 \] ")
        self.lineEdit_2.setReadOnly(True)


        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit.setInputMask(" (0, 0) ")
        self.lineEdit.setReadOnly(True)




        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
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



        self.listWidget.itemSelectionChanged.connect(self.ecrit_piece)
        self.tableWidget.itemSelectionChanged.connect(self.ecrit_coord)
        self.buttonBox.rejected.connect(self.annul)
        self.buttonBox.rejected.connect(self.annul)
        self.buttonBox.accepted.connect(self.joue_piece)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def annul(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.tableWidget.clearSelection()
        self.listWidget.clearSelection()

    def joue_piece(self):

        if self.listWidget.selectedItems() and not self.tableWidget.selectedItems() :
                    row = self.tableWidget.currentRow()
                    col = self.tableWidget.currentColumn()
                    if self.tableWidget.item(row,col) == None:
                        item = QtWidgets.QTableWidgetItem(self.listWidget.currentItem().text())
                        self.tableWidget.setItem(row, col,item )
                        self.tableWidget.item(row,col).setFlags(QtCore.Qt.ItemIsEnabled)
                        self.listWidget.takeItem(self.listWidget.currentRow())
                        self.listWidget.clearSelection()
                        self.tableWidget.clearSelection()
                        self.lineEdit.clear()
                        self.lineEdit_2.clear()



    def ecrit_piece(self):
        self.lineEdit_2.setText((self.listWidget.currentItem().text()))

    def ecrit_coord(self):
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        self.lineEdit.setText('('+ str(row)+', '+str(col)+')')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Jeu de quarto"))
        self.label.setStyleSheet("color: red; font : bold 16px")
        self.label_2.setText(_translate("MainWindow", "Pièce:"))
        self.label_3.setText(_translate("MainWindow", "Coordonéés:"))
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

