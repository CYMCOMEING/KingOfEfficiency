import pyodbc
import os

class DBManager():
    def __init__(self, DBfile) -> None:
        # TODO 检查文件数据库是否安装驱动
        # TODO 判断文件是否合法
        self.DBfile = DBfile
        self.conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+ DBfile +";Uid=;Pwd=;")
        # TODO 检查标和表头

    def insert(self):
        pass

    def delet(self):
        pass

    def select(self):
        pass

    def modify(self):
        pass