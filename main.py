import datetime
import time
import pandas as pd

from handler import api_wialon_dwnObj, api_wialon_reg_fuel

file = 'Заправки.xls'
x1 = pd.ExcelFile(file)
df1 = x1.parse('Sheet1')
df_range = len(df1)

for i in range(df_range):
    try:
        date, time_f = df1["Дата и время"][i].split('   ')
    except:
        try:
            date, time_f = df1["Дата и время"][i].split('  ')
        except:
            date, time_f = df1["Дата и время"][i].split(' ')
    d, m, y = date.split('.')
    h, min = time_f.split(':')
    time_fuel = datetime.datetime(year=int('20'+y), month=int(m), day=int(d), hour=int(h), minute=int(min), second=0)
    time_fuel_unix = int(str(time.mktime(time_fuel.timetuple()))[:-2])
    id_obj = api_wialon_dwnObj(str(df1["Госномер"][i]))
    api_wialon_reg_fuel(str(id_obj), time_fuel_unix, float(df1["Заправка"][i]))