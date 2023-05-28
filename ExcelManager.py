import xlwings as xw


class ExcelManager:

    def __init__(self) -> None:
        self.wb = None

    def open(self, filename: str) -> None:
        """打开Excel"""
        self.wb = xw.Book(filename)

    def insert(self, data: list) -> bool:
        """在活动单元格插入一组数据"""
        if not (self.wb and data):
            return False

        active_range = self.wb.selection
        active_sheet = active_range.sheet
        data_len = len(data)
        insert_ranges = active_sheet.range(
            (active_range.row, 1), (active_range.row, data_len))
        insert_ranges.value = data
    
    def inserts(self, data: list):
        '''一次插入多组数据'''
        for i in data:
            self.insert(i)
            self.move_range()

    def move_range(self, direction: str = 'down') -> None:
        """移动活动单元格"""
        if not self.wb:
            return 
        
        cur_range = self.wb.selection
        add = cur_range.address
        _, col, row = add.split("$") # 列，行
        col = Col2Int(col)
        row = int(row)

        if direction == 'up' and row > 1:
            row -= 1
        elif direction == 'down':
            row += 1
        elif direction == 'left' and col > 1:
            col -= 1
        elif direction == 'right':
            col += 1
        else:
            return
        
        
        sheet = cur_range.sheet
        new_range = sheet.range((row, col)) # 行，列
        new_range.select()
    
    def is_open_workbook(self):
        return bool(self.wb)
        


def Col2Int(s: str) -> int:
    """Excel英文列数转数字"""
    assert (isinstance(s, str))
    for i in s:
        if not 64 < ord(i) < 91:
            raise ValueError('Excel Column ValueError')
    return sum([(ord(n)-64)*26**i for i, n in enumerate(list(s)[::-1])])


def ExcelColumn(n: int) -> str:
    """数字转Excel英文列数"""
    assert (isinstance(n, int) and n > 0)
    num = [chr(i) for i in range(65, 91)]
    ret = []
    while n > 0:
        n, m = divmod(n-1, len(num))
        ret.append(num[m])
    return ''.join(ret[::-1])


if __name__ == '__main__':
    em = ExcelManager()
    em.open(r'E:\桌面\新建 Microsoft Excel 工作表.xlsx')

    # 在活动单元格所在的行，插入10组数据，默认从A开始
    import random
    em.insert([random.randint(0,100) for _ in range(10)])
    em.move_range()
    em.insert([random.randint(0,100) for _ in range(10)])
    em.move_range()