import openpyxl

workbook = openpyxl.Workbook()
# print(workbook.active.title)

# Change name of the sheet
sheetObject = workbook.active
sheetObject.title = "TestSheet1"

print(sheetObject.title)

# Now put data in the sheet
sheetObject['A4'].value = "This is a QA Test"

# Created a new sheet
workbook.create_sheet(title="QA Test")

# Now want to enter the data in 2nd sheet
sheetObject1=workbook['QA Test']
sheetObject1['A3']="+91-123142141"

# Remove Sheet
workbook.remove(workbook["TestSheet1"])

# Saving changes
workbook.save("WriteData.xlsx")