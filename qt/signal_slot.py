import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot

'''
The @Slot() is a decorator that identifies a function as a slot. 
It is not important to understand why for now, but use it always to avoid unexpected behavior.
'''

@pyqtSlot()
def say_hello():
    print("Button clicked, Hello!")

app = QApplication(sys.argv)

button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()

app.exec_()