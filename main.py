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

class FakeTerminal(QtGui.QTextEdit):
    def __init__(self,  parent):
        super(FakeTerminal,  self).__init__(parent)

    def keyPressEvent(self,  event):
        if event.key() == Qt.Key_Return:
            if event.modifiers() == Qt.ControlModifier:
                event = QKeyEvent(QEvent.KeyPress,  Qt.Key_Return, Qt.NoModifier)
            else:
                self.emit(SIGNAL("sendMessage"))
                return

        QTextEdit.keyPressEvent(self,  event)

class MainWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi()

        self.challenge_number = 0
        self.challenge = challenges[self.challenge_number]
        self.challengeLabel.setText("Challenge: " + self.challenge['name'])
        self.challengeText.setText(self.challenge['desc'])
        self.terminalText.setFocus()
        self.show()

    def setupUi(self):
        self.resize(697, 423)
        self.gridLayout = QtGui.QGridLayout(self)
        self.challengeText = QtGui.QTextBrowser(self)
        self.gridLayout.addWidget(self.challengeText, 1, 0, 1, 1)
        self.challengeLabel = QtGui.QLabel(self)
        self.gridLayout.addWidget(self.challengeLabel, 0, 0, 1, 1)
        self.terminalLabel = QtGui.QLabel(self)
        self.gridLayout.addWidget(self.terminalLabel, 0, 1, 1, 1)
        self.terminalText = QtGui.QTextEdit(self)
        self.gridLayout.addWidget(self.terminalText, 1, 1, 1, 1)
        
def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
