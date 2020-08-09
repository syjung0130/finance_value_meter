import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import qApp, QMainWindow, QAction, QApplication
from PyQt5.QtGui import QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Earthquake information")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Data loaded and plotted")

        # Window dimensions
        geometry = qApp.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MainWindow()
    my_window.show()
    app.exec_()