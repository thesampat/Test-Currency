import pandas as pd
import os
from datetime import datetime



"""
Please Refer this Folder Structre to Execute code successfully

Dir-
    -programme.py
    -Datasets/
        -.csv
        -.csv
"""         





pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# collect all csv files into an array
files = []
for file in os.listdir('Datasets'):
    if '.csv' in file:
        files.append(file)

# combine the all datasets into one 
dt = pd.concat((pd.read_csv('Datasets'+'/'+f) for f in files), ignore_index=True)

dt.head()

# rename to column names to remove space
dt.columns = dt.columns.str.replace(' ', '')

# ignore null date values
dt1 = dt[dt['Date'].isnull() == False]

# convert date string to datetime object 
dt1['Date'] = pd.to_datetime(dt1['Date'])

# sort dataset as per date 
dt1 = dt1.sort_values(by='Date')


# progrmme to find currency value based on given country code
def check_currency(code):

    # loop through all columns names
    for col in dt.columns[1:-1]:
        
        # match the given code to column name
        if code in col:

            # ignore null value rows
            data = dt1[dt1[col].isnull()==False][['Date', col]]

            # find min, max, and current value
            sortedc = data.sort_values(col)
            mi = data[data[col]==data[col].min()]
            mx = data[data[col]==data[col].max()]
            cr = data.iloc[-1,:]
                
            print(f'Current value of USD to {code} is {cr.iloc[1]} on {str(cr["Date"]).split(" ")[0]}')
            print(f'Maximum value of USD to {code} is {mx.iloc[0, 1]} on {str(mx["Date"].values[0]).split("T")[0]}')
            print(f'Minimum value of USD to {code} is {mi.iloc[0, 1]} on {str(mi["Date"].values[0]).split("T")[0]}')
                
            return
    print('Wrong Code, Please Try Again!')

code = str(input('Enter the Currency Code : '))
if len(code) != 3:
    print('Please enter valid Currency Code')
else:
    check_currency(code)
