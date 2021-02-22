import csv
import datetime
import openpyxl

wb = openpyxl.load_workbook('Finance Tracker.xlsx')
ws = wb.active



"""
ss = ezsheets.Spreadsheet('1X-BALp-_4x9ex2p6DYMOiJC_ZKPqQd0-esM1uv7qSmg')
sh1 = ss[0]  # sh1 = Transactions Sheet
sh2 = ss[1]  # sh2 = Monthly Balance Sheet

with open('stmt.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    row_count = 1
    for row in reader:
        if row_count == 2:
            starting_balance = row[4][row[4].index('"') + 1:len(row[4]) - 1]
            starting_balance = float(starting_balance)
            start_date = row[4][0:10]
        if row_count == 3:
            totalDeposit = row[1][row[1].index('"') + 1: len(row[1]) - 1]
            totalDeposit = float(totalDeposit)
        if row_count == 4:
            totalWithdraw = row[1][row[1].index('"') + 1: len(row[1]) - 1]
            totalWithdraw = float(totalWithdraw)
        if row_count == 5:
            ending_date = row[4][0:10]
        if row_count >= 9:
            ws.append(row[0], row[1], '', '', row[2], row[3])
            print(row)
        row_count += 1


ending_balance = starting_balance + totalDeposit + totalWithdraw

month_number = start_date[0:2]


datetime_object = datetime.datetime.strptime(month_number, "%m")
month_name = datetime_object.strftime("%B")

print()
print(month_name + " Statement")
print()
print("Start Date: " + start_date)
print("End Date: " + ending_date)
print("Starting Balance: " + str(starting_balance))
print("Deposits: " + str(totalDeposit))
print("Withdrawls: " + str(totalWithdraw))
print("Ending Balance: " + str(ending_balance))
print(sh1.frozenRowCount)
"""


