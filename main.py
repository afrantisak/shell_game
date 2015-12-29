#!/usr/bin/env python
import sys
import PyQt4
import PyQt4.uic
from PyQt4 import QtGui

mainWindowUi = PyQt4.uic.loadUiType("main.ui")[0]

class MainWindow(QtGui.QMainWindow, mainWindowUi):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
