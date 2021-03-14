import openpyxl

book = openpyxl.open('112.xlsx', read_only=True)

sheet = book.active

print(sheet[13][0].value)

fmt = '|{:50} | {:9.4f} | {:9.4f}|'

for row in range(13, sheet.max_row):
    name = sheet[row][0].value
    debet_start = sheet[row][3].value
    debet_end = sheet[row][11].value
    print(fmt.format(name, debet_start, debet_end))
