import sys
from PyQt5.QtWidgets import qApp, QMainWindow, QAction, QApplication
from ui.main_window import MainWindow
from ui.main_widget import Widget

app = QApplication(sys.argv)

widget = Widget()
window = MainWindow(widget)
window.show()
sys.exit(app.exec_())
