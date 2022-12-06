


class SQLGenerator():
    def __init__(self) -> None:
        pass


    @staticmethod
    def get_sql_inster(data: dict, table: str):
        """
        将字典数据转行成sql语句
        return: 返回sql和参数 insert into <表名> (字段1, 字段2...) values (?,?...)
        """
        # TODO 判断数据类型
        values = []
        keys = ''
        parm = ''
        for k, v in data.items():
            keys += k + ','
            parm += '?,'
            values.append(v)
        
        if len(keys) > 0:
            keys = keys[:-1]
            parm = parm[:-1]
        
        sql = "insert into {} ({}) values ({});".format(table, keys, parm)
        return sql, values

    @staticmethod
    def get_sql_modify(data: dict, where_data: list, table:str):
        """
        将字典数据转成sql语句
        data: 字典类型，新数据
        where_data: 列表类型，第一个是字段，第二个是值，使用 = 关系
        table: 表名
        return: 返回sql语句和参数 UPDATE <表名> SET 字段1=?, 字段2=?, ... WHERE 字段=?;
        """
        keys = ''
        values = []
        for k, v in data.items():
            keys += k + '=?, '
            values.append(v)

        if len(keys) > 0:
            keys = keys[:-2]
            values.append(where_data[1])

        sql = "update {} set {} where {}=?".format(table, keys, where_data[0])
        return sql, values

    @staticmethod
    def get_sql_delete(where_data: list, table:str):
        """
        将列表转成sql语句
        where_data: 列表类型，第一个是字段，第二个是值，使用=关系
        table: 表名
        return: 返回sql语句和参数 DELETE FROM <表名> WHERE 字段=?;
        """
        sql = "delete from {} where {}=?".format(table, where_data[0])
        return sql, [where_data[1], ]

def test():
    sg = SQLGenerator()
    res = sg.get_sql_inster({"name": "张三", "age": 18}, "person")
    print(res)

if __name__ == "__main__":
    test()