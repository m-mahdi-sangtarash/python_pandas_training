import pandas as pd

data = {"Physic": [18, 12, 19],
        "Chemistry": [16.25, 15, 20],
        "Math": [14, 13, 18],
        "literature": [17, 15, 17]}

data_f = pd.DataFrame(data, index=["Ali", "Mohammad", "Reza"])
e_writer = pd.ExcelWriter("Lessons Grades.xlsx", engine="xlsxwriter")
data_f.to_excel(e_writer, sheet_name="grades")
e_writer.save()
