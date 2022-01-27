import openpyxl

wb_obj = openpyxl.Workbook()

sheet_obj = wb_obj.active

team_wsr = (
    ("10-12-2021", "Theory", "program"),
    ("11-12-2021", "preparation","interview"))
for data in team_wsr:
    sheet_obj.append(data)

wb_obj.save("C:\\users\\visweswar\\Desktop\\team.xlsx")


