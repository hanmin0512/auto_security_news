import Crwaling, ExcelAuto

crwal = Crwaling.Crwal("http://www.boannews.com")
excel = ExcelAuto.Excel()
title = ["제목", "URL"]
if __name__ == "__main__":
    crwal.ready()
    crwal.crwalTitle()
    crwal.crwalUrl()
    
    excel.write_column(title)
    excel.write_row(1, crwal.title_list)
    excel.write_row(2, crwal.url_list)
    excel.save_excel()