from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QPainter
from PyQt5 import QtChart
from PyQt5.QtWidgets import *
import sys
from ui.table_model import CustomTableModel
from scrap.dart.finance_sheet import FinanceSheetAdapter
from scrap.krx.stock_code import StockCode
from scrap.krx.stock_finance_indicator import StockFinanceIndicator

'''
https://stackoverflow.com/questions/58274166/cannot-import-pyqtchart-in-python-3-7
pyqt5에서 QtChart를 사용하기 위해서는 아래 패키지를 설치해주어야한다.
python -m pip install PyQt5==5.13 PyQtChart==5.13
그리고 import할 때에는 아래 처럼 해주어야 한다.
from PyQt5 import QtChart
'''

class Widget(QWidget):
    # def __init__(self, data):
    def __init__(self):
        QWidget.__init__(self)

        self.grp_box = QGroupBox("재무 정보")
        self.create_widgets()
        self.create_finance_table_model()
        self.create_valuation_table_model()

        # Left layout
        self.create_finance_table_view()
        self.create_valuation_table_view()
        self.left_inner_layout = QVBoxLayout()
        self.left_inner_layout.addWidget(self.label_stock_code_search)
        self.left_inner_layout.addWidget(self.edit_corp_name)
        self.left_inner_layout.addWidget(self.edit_corp_code)
        self.left_inner_layout.setAlignment(Qt.AlignTop)
        self.grp_box.setLayout(self.left_inner_layout)

        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.grp_box)
        self.left_layout.addWidget(self.finance_table_view)

        # Right Layout - # Creating QChartView: 매출액, 순이익, 자산 증가 추세
        self.chart = QtChart.QChart()
        self.chart.setAnimationOptions(QtChart.QChart.AllAnimations)
        self.add_series("Magnitude (Column 1)", [0, 1])
        self.chart_view = QtChart.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Right Layout - Add charg widget
        self.right_layout = QVBoxLayout()
        # size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # size.setHorizontalStretch(4)
        # self.chart_view.setSizePolicy(size)
        self.right_layout.addWidget(self.chart_view)

        # QWidget Layout
        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)

        # Set the layout to the QWidget
        self.setLayout(self.main_layout)
    
    def create_widgets(self):
        # Create Widgets
        self.label_stock_code_search = QLabel("종목 코드 조회:")
        self.edit_corp_name = QLineEdit("회사명을 입력하고 엔터를 입력하세요.")
        self.edit_corp_code = QLineEdit("종목 코드:")
        self.edit_corp_name.returnPressed.connect(self.update_codes)
    
    def create_finance_table_model(self):
        # Getting the Model - PER, PBR, EPS, ROE를 table로
        self.indicator = StockFinanceIndicator()
        dataframe = self.indicator.get_finance_dataframe_by_code("005930")
        self.finance_table_model = CustomTableModel(dataframe)
    
    def create_finance_table_view(self):
        # Creating a QTableView
        self.finance_table_view = QTableView()
        self.finance_table_view.setModel(self.finance_table_model)
        self.init_table_headers()
        self.size.setHorizontalStretch(1)
        self.finance_table_view.setSizePolicy(self.size)
        # self.main_layout.addWidget(self.finance_table_view)
    
    def init_table_headers(self):
        # QTableView Headers
        self.horizontal_header = self.finance_table_view.horizontalHeader()
        self.vertical_header = self.finance_table_view.verticalHeader()
        self.horizontal_header.setSectionResizeMode(
                            QHeaderView.ResizeToContents
                            )
        self.vertical_header.setSectionResizeMode(
                            QHeaderView.ResizeToContents
        )
        self.horizontal_header.setStretchLastSection(True)
        self.size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def create_valuation_table_model(self):
        print('create_valuation_table_model')

    def create_valuation_table_view(self):
        print('create_valuation_table_view')
    
    # Greets the user
    def get_code_text(self):
        print("종목 정보 %s" % self.edit_corp_name.text())

    def update_codes(self):
        self.stock_code = StockCode()
        self.stock_code.update_stock_codes()
        try:
            self.str_name = self.edit_corp_name.text()
            code = self.stock_code.get_stock_code_by_name(self.str_name)#edit_corp_name
            print("stock_code : {}".format(code))
            self.str_code = '%06d'%code
            self.edit_corp_code.setText(self.str_code)
            dataframe = self.indicator.get_finance_dataframe_by_code(self.str_code)
            self.finance_table_model.update_data(dataframe)
            
        except ValueError:
            print("invalid corp name: {}".format(self.edit_corp_name.text()))
            self.edit_corp_code.setText("잘못된 회사명입니다.")
    
    def add_series(self, name, columns):
        # Create QLineSeries
        self.series = QtChart.QLineSeries()
        self.series.setName(name)

        # Filling QLineSeries
        for i in range(self.finance_table_model.rowCount()):
            # Getting the data
            t = self.finance_table_model.index(i, 0).data()

            x = self.finance_table_model.index(i, 0).data()
            y = self.finance_table_model.index(i, 1).data()

            self.series.append(0, 0)
            
        self.chart.addSeries(self.series)

        # Setting X-axis
        self.axis_x = QtChart.QDateTimeAxis()
        self.axis_x.setTickCount(10)
        self.axis_x.setFormat("dd.MM (h:mm)")
        self.axis_x.setTitleText("Date")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        # Setting Y-axis
        self.axis_y = QtChart.QValueAxis()
        self.axis_y.setTickCount(10)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Magnitude")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        # Getting the color from QChart to use it on the QTableView
        self.finance_table_model.color = "{}".format(self.series.pen().color().name())
