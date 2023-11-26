import openpyxl

class Excel:
    def __init__(self):
        self.workbook = openpyxl.Workbook()
        self.column = []
        self.worksheet = self.workbook.active
    
    #파일에 내용을 쓴다.
    def set_column(self, number):
        for i in range(number):
            self.column.append(chr(65+i)+str(1))
    
    def write_column(self, column_list):
        size = len(column_list)
        self.set_column(size)
        
        for i in range(size):
            self.worksheet[self.column[i]] = column_list[i]
            
    def write_row(self, col ,data):
        for i in range(2,len(data)+2):
            self.worksheet.cell(row = i, column = col, value = data[i-2])
            
    
    def save_excel(self):
        self.workbook.save("example.xlsx")

#write_column = ["제목", "URL"]
#E = Excel()
#E.write_column(write_column)
#E.save_excel()
        