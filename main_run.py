from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, pyqtSignal
from ui.Ui_mainpage import Ui_MainWindow
from addData import AddDataPage
import sys
from DBManager import DBManager
from models.product import Product

class MainPage(QMainWindow, Ui_MainWindow):    
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)

        # 绑定增加按钮事件
        self.btn_add.clicked.connect(self.btn_add_clicked)

        self.dbm = DBManager()
        self.show_data()

    def btn_add_clicked(self):
        # 增加按钮事件函数
        childDialog = AddDataPage(self)
        childDialog.get_data_connect(self.add_data) # 子窗口信号绑定
        childDialog.show()

    def add_data(self, p:Product):
        # 增加数据到数据库
        self.dbm.add(p)

    
    def show_data(self):
        # 展示数据
        datas = self.dbm.query(Product)
        header = ['id', "产品名", '参数', '分类']
        row_len = len(datas)
        column_len = len(header)

        # 设置表格行列
        self.model = QStandardItemModel(row_len, column_len)

        # 设置表头
        self.model.setHorizontalHeaderLabels(header)

        # 表格控件关连Model
        self.tableView_main.setModel(self.model)

        # 填充数据
        for row in range(0, row_len):
            self.model.setItem(row, 0, QStandardItem(str(datas[row].id)))
            self.model.setItem(row, 1, QStandardItem(datas[row].name))
            self.model.setItem(row, 2, QStandardItem(datas[row].parameter))
            self.model.setItem(row, 3, QStandardItem(datas[row].category))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mp = MainPage()
    mp.show()
    sys.exit(app.exec_())