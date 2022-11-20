import pyodbc
import os

class DBManager():
    def __init__(self, DBfile) -> None:
        # TODO 检查文件数据库是否安装驱动
        # TODO 判断文件是否合法
        # TODO 注意线程安全
        self.DBfile = DBfile
        self.conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+ DBfile +";Uid=;Pwd=;")
        # TODO 检查标和表头


    def get_all_table(self):
        """
        获取所有表名
        """
        curs = self.conn.cursor()
        tables = []
        for table in curs.tables(tableType='TABLE'):
            tables.append(table)
        curs.close()
        return tables

    def insert(self, sql, *params):
        """
        插入数据
        sql格式: insert into 表(字段1, 字段2...) value (?,?...)
        """
        curs = self.conn.cursor()
        curs.execute(sql, params)
        curs.commit()
        curs.close()

    def delet(self, sql, *params):
        """
        删除数据
        sql格式: delete from 表 where 字段 == ?
        """
        curs = self.conn.cursor()
        curs.execute(sql, params)
        del_count = curs.rowcount # 删除了多少条数据
        curs.commit()
        curs.close()
        return del_count

    def select(self, sql):
        """
        查询数据
        sql格式: select 字段1,字段2... from 表
        return: 返回列表，每项内容是一个元组(数据1,数据2...)
        """
        curs = self.conn.cursor()
        curs.execute(sql)
        res = curs.fetchall()
        curs.close()
        return res

    def modify(self, sql, *params):
        """
        修改数据
        sql格式: update 表 set 字段 = ? where 字段 = ?
        """
        curs = self.conn.cursor()
        curs.execute(sql, params)
        curs.commit()
        curs.close()