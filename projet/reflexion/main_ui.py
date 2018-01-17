# -*- coding: utf-8 -*-

import ui_interact
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui=ui_interact.Ui_interact(MainWindow)
    ui.setupUibis(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

