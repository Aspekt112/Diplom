#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from diplom_ui import Ui_MainWindow
from research_packets import *

from PyQt4 import QtGui


def research_packets(ui):
    TMIsize = ui.comboBox.currentText()
    ErrorProbability = ui.comboBox_2.currentText()
    PacketsNumber = ui.lineEdit.text()

    print(TMIsize, ErrorProbability, PacketsNumber)
    matrix = generate_tmi_matrix(TMIsize)
    print(matrix)


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # ui.comboBox.activated[str].connect(onActivated)
    ui.pushButton.clicked.connect(lambda: research_packets(ui))
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
