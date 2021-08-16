import gspread
import pandas as pd
import os

# Documentation: https://gspread.readthedocs.io/en/latest/oauth2.html
# Linux: Move service_account.json to ~/.config/gspread/service_account.json
# Windows: Add %APPDATA%\gspread\service_account.json to PATH variable 
gc = gspread.service_account()

#Or move service_account.json to another location
#gc = gspread.service_account(filename='path/to/the/downloaded/file.json')

# Open a sheet from a spreadsheet 
sh = gc.open("Aug 2021 - Course Data")

worksheet_list = sh.worksheets()

# Remove Help Info Sheet
worksheet_list.pop(0)

subjects = ['sem-3', 'mth','hss','ecs','chm','phy','bio']
header = ['courses','instructors']

for i,worksheet in enumerate(worksheet_list):
    df_temp = pd.DataFrame(worksheet.get_all_records())
    
    if i%2==0:
        df_temp.to_csv(os.path.join("data",subjects[i//2]+"_"+header[0]+".csv"))
    else:
        df_temp.to_csv(os.path.join("data",subjects[i//2]+"_"+header[1]+".csv"))
