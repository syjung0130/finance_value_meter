from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor
import pandas as pd

# https://stackoverflow.com/questions/17697352/pyqt-implement-a-qabstracttablemodel-for-display-in-qtableview

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)

    def load_data(self, data):
        print('load_data')
        # print(data)
        # print(data.shape)
        # print('row, col: ({0}, {1})'.format(data.shape[0], data.shape[1]))
        # print("columns: {}".format(list(data.columns.values)))
        self.df = data
        self.row_count = data.shape[0]
        self.column_count = data.shape[1]
        self.columns_list = list(data.columns.values)

    # https://stackoverflow.com/questions/45359569/how-to-update-qtableview-on-qabstracttablemodel-change
    def update_data(self, data):
        self.df = data
        for i in range(self.row_count):
            for j in range(self.column_count):
                self.dataChanged.emit(self.index(i, j), self.index(i, j))

    def rowCount(self, parent=QModelIndex()):
        return self.row_count
    
    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.columns_list[section]
        else:
            return "{}".format(section)
    
    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            return self.df.iloc[row][column]
        elif role == Qt.BackgroundColorRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight
        
        return None
