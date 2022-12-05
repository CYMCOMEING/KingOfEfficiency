


class SQLGenerator():
    def __init__(self) -> None:
        pass


    @staticmethod
    def get_sql_inster(data: dict, table: str) -> str:
        """
        将字典数据转行成sql语句
        return: 返回sql和参数 insert into 表(字段1, 字段2...) value (?,?...)
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


def test():
    sg = SQLGenerator()
    res = sg.get_sql_inster({"name": "张三", "age": 18}, "person")
    print(res)

if __name__ == "__main__":
    test()