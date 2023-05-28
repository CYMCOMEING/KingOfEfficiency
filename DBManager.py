from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import reflection
from sqlalchemy.schema import MetaData
from sqlalchemy import engine, create_engine, or_

class DBManager():

    def __init__(self, file: str) -> None:
        
        connection_string = (
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            f"DBQ={file};" # 要绝对路径
            r"ExtendedAnsiSQL=1;"
        )
        print(connection_string)
        connection_url = engine.URL.create(
            "access+pyodbc",
            query={"odbc_connect": connection_string}
        )
        self.engine = create_engine(connection_url)
        # Base.metadata.create_all(self.engine) # 创建表
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.insp = reflection.Inspector.from_engine(self.engine)
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)
        self.table = None
    
    def __del__(self):
        self.session.close()

    def get_tables_name(self):
        '''获取所有表名'''
        return [i for i in self.metadata.tables.keys()]
    
    def set_table(self, table_name):
        '''获取特定表的对象'''
        self.table = self.metadata.tables[table_name]

    def get_table_col(self):
        '''获取表头'''
        if self.table == None:
            return []
        return [i for i in self.table.c.keys()]
    
    def query(self, index=None):
        '''查询数据'''
        if self.table == None:
            return []

        
        # 条件查询，全字段匹配
        if index != None:
            result = self.session.query(self.table).filter(or_(*[column.like(f'%{index}%') for column in self.table.c])).all()
            return result
        
        # 查询全部结果
        result = self.session.query(self.table).all()
        return result


if __name__ == "__main__":
    p1 = Part(id = 2, series='', name_='', description='', model='', manufacturer='', num=0, units='', remarks='', subcategoryID=1)
    p2 = Part(id = 3, series='', name_='', description='', model='', manufacturer='', num=0, units='', remarks='', subcategoryID=1)
    p3 = Part(id = 4)
    dbm = DBManager(r'G:\Project\KingOfEfficiency\TEST.accdb')
    # dbm.add([p1,p2,p3])

    # res = dbm.query_all(Part)
    # res = dbm.query(Product, Product.parameter == "24V")
    # for i in res:
    #     print(i.__dict__)


    # p1.name_ = "C36"
    # dbm.add(p1)
    # dbm.delete(p2)

    # 获取数据库所有表名
    # print(dbm.get_table_columns('part'))
    # 字段表具体数据
    # print(dbm.insp.get_columns('part'))

    # print(dbm.get_tables_name())
    dbm.set_table('Part')
    # print(dbm.get_table_col())
    result = dbm.query('3')
    for row in result:
        print(row)
