import openpyxl
import csv

wb = openpyxl.load_workbook('sale_report_1_aug_12_aug.xlsx')
sh = wb.get_active_sheet()
with open('test.csv', 'w') as f:  # open('test.csv', 'w', newline="") for python 3
    c = csv.writer(f)
    for r in sh.rows:
        c.writerow([cell.value for cell in r])