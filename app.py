from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QMenu, QAction
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSignal, QItemSelectionModel, Qt

import sys
import os

from ui.Ui_mainpage import Ui_MainWindow
from DBManager import DBManager
from ExcelManager import ExcelManager


class MainPage(QMainWindow, Ui_MainWindow):
    _show_data_signal = pyqtSignal(list, list)

    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)

        # 绑定事件
        self.btn_open_file.clicked.connect(self.btn_open_file_clicked)
        self.listWidget_table.itemClicked.connect(self.show_table_data)
        self.btn_sreach.clicked.connect(self.btn_sreach_clicked)
        self.lineEdit_index.textChanged.connect(self.lineEdit_index_change)
        self.btn_open_excel.clicked.connect(self.btn_open_excel_clicked)

        # 表格设置右键菜单
        self.tableView_main.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_main.customContextMenuRequested.connect(self.show_menu)


        # 绑定槽
        self._show_data_signal.connect(self.show_data)

        # 数据库实例
        self.dbm = None
        # Excel控制示例
        self.em = ExcelManager()


    def btn_sreach_clicked(self):
        """按钮搜索事件"""
        index = self.lineEdit_index.text()
        if not index:
            index = None
    
        self.sreach(index)

    def lineEdit_index_change(self, text):
        '''输入栏内容改变事件'''
        self.sreach(text)

    def sreach(self, index):
        '''搜索'''
        if not self.dbm:
            return
        res = self.dbm.query(index)
        header = self.dbm.get_table_col()
        self._show_data_signal.emit(res, header)
            

    def btn_open_file_clicked(self):
        """打开数据库文件事件"""
        file, _ = QFileDialog.getOpenFileName(self, '选择数据库文件', '.', 'Microsoft Access (*.mdb, *.accdb)')
        if file and os.path.exists(file):
            self.dbm = DBManager(file)
            self.label_db_path.setText(os.path.abspath(file))
            tables = self.dbm.get_tables_name()
            self.show_table(tables)
    
    def show_table(self, data: list):
        '''列表显示内容'''
        if not data:
            return

        self.listWidget_table.clear()
        self.listWidget_table.addItems(data)
        
        # 手动触发显示第一个表数据
        self.listWidget_table.setCurrentItem(self.listWidget_table.item(0), QItemSelectionModel.SelectCurrent)
        self.listWidget_table.itemClicked.emit(self.listWidget_table.item(0))

    def show_table_data(self, item: QListWidgetItem):
        '''列表点击事件，选择表'''
        if not self.dbm:
            return
        
        self.dbm.set_table(item.text())
        res = self.dbm.query()
        header = self.dbm.get_table_col()
        self._show_data_signal.emit(res, header)

    def show_data(self, datas, header):
        '''显示数据'''

        # 设置表格行列
        # self.model = QStandardItemModel(row_len, column_len)
        self.model = QStandardItemModel()

        # 设置表头
        self.model.setHorizontalHeaderLabels(header)

        # 表格控件关连Model
        self.tableView_main.setModel(self.model)

        # 填充数据
        for row in range(0, len(datas)):
            for col in range(len(header)):
                self.model.setItem(row, col, QStandardItem(str(datas[row][col])))

    def btn_open_excel_clicked(self):
        '''打开Excel文件按钮事件'''
        file, _ = QFileDialog.getOpenFileName(self, '选择Excel文件', '.', 'Microsoft Excel (*.xlsx)')
        if file and os.path.exists(file):
            self.em.open(file)
            self.label_excel_path.setText(os.path.abspath(file))

    def show_menu(self, position):
        """显示右键菜单"""
        menu = QMenu(self.tableView_main)

        # 添加菜单项
        delete_action = QAction("插入Excel", self.tableView_main)
        menu.addAction(delete_action)

        # 显示菜单
        action = menu.exec_(self.tableView_main.mapToGlobal(position))

        # 处理菜单项的动作
        if action == delete_action:
            selection_model = self.tableView_main.selectionModel()
            selected_indexes = selection_model.selectedIndexes()
            row_choice = set()  # 记录那行被选中
            for index in selected_indexes:
                row_choice.add(index.row())

            # 获取每行的数据
            model = self.tableView_main.model()
            max_col = model.columnCount()
            insert_date = []
            for row in row_choice:
                row_data = []
                for col in range(max_col):
                    index = model.index(row, col)
                    value = model.data(index, Qt.DisplayRole)
                    row_data.append(value)
                insert_date.append(row_data)

            self.em.inserts(insert_date)
            # print(insert_date)
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mp = MainPage()
    mp.show()
    sys.exit(app.exec_())