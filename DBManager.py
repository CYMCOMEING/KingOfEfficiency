from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from models.product import Base

class DBManager():

    def __init__(self) -> None:
        # 路径要绝对路径
        connection_string = (
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"DBQ=G:\Project\KingOfEfficiency\效率之王.accdb;"
            r"ExtendedAnsiSQL=1;"
        )
        connection_url = sa.engine.URL.create(
            "access+pyodbc",
            query={"odbc_connect": connection_string}
        )
        self.engine = sa.create_engine(connection_url)
        Base.metadata.create_all(self.engine) # 创建表
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # 增加数据, 修改数据
    def add(self, data):
        if isinstance(data, (list,tuple)):
            self.session.add_all(data)
        else:
            self.session.add(data)
        self.session.commit()

    # 删除数据
    def delete(self, data):
        self.session.delete(data)
        self.session.commit()

    # 查询数据
    # 传入数据的对象，使用对象中的__repr__()函数的返回值
    def query(self, class_data, *where):
        if where:
            # 带条件查询
            query_result = self.session.query(class_data).filter(*where)
        else:
            query_result = self.session.query(class_data).all()
        # for result in query_result:
        #     print(f"查询结果为: {result}")
        return query_result

if __name__ == "__main__":
    from models.product import Product
    p1 = Product(id=1001, name="交流接触器", parameter="C32", category="电器")
    p2 = Product(id=1002, name="电磁继电器", parameter="24V", category="电器")
    dbm = DBManager()
    # dbm.add([p1,p2])

    # res = dbm.query(Product)
    res = dbm.query(Product, Product.parameter == "24V")
    for i in res:
        print(i)


    # p1.parameter = "C36"
    # dbm.add(p1)
    # dbm.delete(p2)

    