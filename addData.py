from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal, Qt
from ui.Ui_addData import Ui_Dialog
from models.product import Product


class AddDataPage(QDialog, Ui_Dialog):
    # 信号，用于发射数据
    _add_signal = pyqtSignal(Product)

    def __init__(self, parent=None):
        super(AddDataPage, self).__init__(parent)
        self.setupUi(self)

        self.setWindowModality(Qt.ApplicationModal) # 阻塞父窗口

        # 增加按钮事件绑定函数
        self.btn_ok.clicked.connect(self.but_ok_clicked)


    def but_ok_clicked(self):
        # 增加按钮事件函数
        if self.lineEdit_name.text():
            p = Product()
            p.name = self.lineEdit_name.text()
            p.parameter = self.lineEdit_parameter.text()
            p.category = self.lineEdit_category.text()
            self.add_signal.emit(p) # 把新数据发射出去
            self.close()
        else:
            # 这里应该弹出一个警告
            print("name没写")
    
    def get_data_connect(self, fun):
        # 绑定槽
        self._add_signal.connect(fun)