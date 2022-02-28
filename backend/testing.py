import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from time import time
from datetime import datetime, timedelta

start_time = time()

#energy_meters_df = pd.read_excel('data/VIS Målere.xlsx')
# Remove leading and trailing whitespace in cells with value of type string
#energy_meters_df = energy_meters_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# parse_dates=['Unnamed: 0']

raw_esave_tables_dict = pd.read_excel(
    'data/EsaveExport_Trondheim Kommune_Trondheim_10121314.xls', decimal=',', sheet_name=None)
raw_esave_tables_list = raw_esave_tables_dict.values()
for table in raw_esave_tables_list:
    table.rename(columns={'Unnamed: 0': 'datetime'}, inplace=True)
    table['datetime'] = pd.to_datetime(table['datetime'], dayfirst=True)
    table.set_index('datetime', inplace=True)
    table.sort_index()
raw_esave_table = pd.concat(raw_esave_tables_list, axis=1, ignore_index=False)

stop_time = time()
elapsed_time = stop_time - start_time
print(f'Used {elapsed_time:.2f} seconds to read xls files')
