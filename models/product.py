from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), default=None, nullable=False, comment="产品名称")
    parameter = Column(String(20), default=None, comment="参数")
    category = Column(String(20), default=None, comment="分类")

    def __repr__(self) -> str:
        return "Product: id:{Id}, name:{Name}, parameter:{Parameter}, category:{Category}".format(
            Id = self.id,
            Name = self.name,
            Parameter = self.parameter,
            Category = self.category
        )

if __name__ == "__main__":
    p = Product(id=1, name="交流接触器", parameter="C32", category="电器")
    print(p)