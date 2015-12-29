#!/usr/bin/env python
import sys
import signal
import PyQt4
import PyQt4.uic
from PyQt4 import QtGui

challenges = [{'name': 'Go Home',
               'desc': 'This is your first challenge:  You need to go home.  Home is represented by the tilde ("~").',
               'answer': 'cd ~'},
              {'name': 'Look around',
               'desc': '"ls" stands for "list" and it tells you what is in your current room',
               'answer': 'ls'},
              ]

mainWindowUi = PyQt4.uic.loadUiType("main.ui")[0]
class MainWindow(QtGui.QDialog, mainWindowUi):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.challenge_number = 0
        self.challenge = challenges[self.challenge_number]
        self.challengeLabel.setText("Challenge: " + self.challenge['name'])
        self.challengeText.setText(self.challenge['desc'])
        self.terminalText.setFocus()
        self.show()
        
def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
