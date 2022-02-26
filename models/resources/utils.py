import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import time
from datetime import datetime
from sklearn.model_selection import train_test_split

vis_path = 'models/resources/data/VIS Målere.xlsx'
esave_path = 'models/resources/data/EsaveExport_Trondheim Kommune_Trondheim_10121314.xls'
et_path = 'models/resources/data/ET Kurver.xlsx'
sensor_types = ['Fastkraft', 'Fjernvarme', 'Varme', 'Elkjel', 'Kjøling']

class et_curve():
    def __init__(self, baseline, dx, dy):
        self.baseline = baseline
        self.dx = dx
        self.dy = dy

    def expected(self, temperature):
        if temperature < self.dx[0]:
            # TODO improve this prediction
            return linear_interpolation(temperature, self.dx[0], self.dy[0], self.dx[1], self.dy[1])
        if temperature > self.dx[-1]:
            return self.dy[-1]

        for i in range(len(self.dx) - 1):
            if self.dx[i] <= temperature and temperature <= self.dx[i+1]:
                return linear_interpolation(temperature, self.dx[i], self.dy[i], self.dx[i+1], self.dy[i+1])

    def plot(self):
        for x, y in zip(self.dx, self.dy):
            plt.plot(x, y, 'rx', markersize=16)

        for x in range(-30, 30):
            prediction = self.expected(x)
            plt.plot(x, prediction, 'go')

    def expected_dfs(self, df):
        df['et-expected'] = df['temperature'].apply(self.expected)
        return df

def prepare_data(meters_data, time_steps, split_ratio=0):
    meters_data.dropna(axis=1, inplace=True)

    X = []
    for i in range(len(meters_data.values) - time_steps + 1):
        X.append(meters_data.values[i : (i + time_steps)])

    X = np.stack(X)
    # min-max normalization
    X = (X - X.min()) / (X.max() - X.min())
    # split training and test data
    if split_ratio:
        return train_test_split(X, test_size=split_ratio)
    return X

def linear_interpolation(x, x0, y0, x1, y1):
    slope = (y1 - y0) / (x1 - x0)
    return y0 + (x - x0) * slope

def et_curve_from_pandas_row(row: pd.core.series.Series) -> et_curve:
    baseline = row['Grunnlast']

    dx = []
    dy = []
    for i in range(1,7):
        x = row[f'DX{i}']
        y = row[f'DY{i}']
        if (not np.isnan(x)) and (not np.isnan(y)):
            dx.append(x)
            dy.append(y)

    return et_curve(baseline, dx, dy)

def load_meters_data(esave_path=esave_path):
    """
    Loads all meter data from all sheets in the given excel file.
    """
    meters_data = pd.read_excel(esave_path, decimal=',', sheet_name=None)
    meters_data_list = meters_data.values()
    for table in meters_data_list:
        table.rename(columns={table.columns[0]: 'datetime'}, inplace=True)
        table['datetime'] = pd.to_datetime(table['datetime'], dayfirst=True)
        table.set_index('datetime', inplace=True)
        table.sort_index()
    meters_data = pd.concat(meters_data_list, axis=1, ignore_index=False)
    return meters_data

def load_and_prepare_building_dfs(vis_path=vis_path, esave_path=esave_path):
    start_time = time()
    energy_meters_df = pd.read_excel(vis_path)
    # Remove leading and trailing whitespace in cells with value of type string
    energy_meters_df = energy_meters_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    raw_esave_tables_dict = pd.read_excel(esave_path, decimal=',', sheet_name=None)
    raw_esave_tables_list = raw_esave_tables_dict.values()
    for table in raw_esave_tables_list:
        table.rename(columns={table.columns[0]: 'datetime'}, inplace=True)
        table['datetime'] = pd.to_datetime(table['datetime'], dayfirst=True)
        table.set_index('datetime', inplace=True)
        table.sort_index()
    raw_esave_table = pd.concat(raw_esave_tables_list, axis=1, ignore_index=False)

    buildings = {}
    current_building = None
    for _, row in energy_meters_df.iterrows():
        # if current row is a building not a sensor create a new dict to store all sensors for that building
        if row['Objekt'] == 'Bygg':
            current_building = {}
            for sensor_type in sensor_types:
                current_building[sensor_type] = {}
            buildings[row['Navn']] = current_building
            continue
        
        sensor_type = row['Type']
        if sensor_type in sensor_types:
            name = row['Navn']
            sensor_id = row['Formel']
            current_building[sensor_type][name] = sensor_id

    # Create a dictionary that contains a dataframe for each building that have column for each sensor type (e.g. Fjernvarme or Fastkraft)
    building_dfs = {}
    for building_name, sensor_type_dict in buildings.items():

        sensor_type_series = {}
        for sensor_type, sensor_dict in sensor_type_dict.items():
            for sensor_id in sensor_dict.values():
                if sensor_id in raw_esave_table.columns:
                    sensor_series = raw_esave_table[sensor_id]
                    if not sensor_type in sensor_type_series:
                        sensor_type_series[sensor_type] = sensor_series
                    else:
                        sensor_type_series[sensor_type] = sensor_type_series[sensor_type] + sensor_series
        if sensor_type_series:
            building_dfs[building_name] = pd.DataFrame(sensor_type_series)
            building_dfs[building_name].sort_index()

    # Create a column in each building dataframe that is the total energy consumption, i.e. the sum of all other columns.
    for building_df in building_dfs.values():
        building_df['Totalt'] = building_df[list(building_df.columns)].sum(axis=1)

    print('Data loaded in {} seconds'.format(time() - start_time))
    return building_dfs

def load_and_prepare_et_curve_dfs(et_path=et_path):
    energy_temperature_df = pd.read_excel(et_path)
    # Remove leading and trailing whitespace in column names
    energy_temperature_df.columns = energy_temperature_df.columns.str.strip()
    # Remove leading and trailing whitespace in cells with value of type string
    energy_temperature_df = energy_temperature_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    et_curve_dfs = {}
    for _, row in energy_temperature_df.iterrows():
        building_name = row['Bygg']
        valid_from_str = row['Fra']
        valid_from = datetime.strptime(valid_from_str, '%d.%m.%Y')

        building_et_curve = et_curve_from_pandas_row(row)

        if not building_name in et_curve_dfs:
            et_curve_dfs[building_name] = {}
        
        et_curve_dfs[building_name][valid_from] = building_et_curve

    return et_curve_dfs

"""
Normalizes buildings by either min-max scaling or standard-score.
https://en.wikipedia.org/wiki/Normalization_(statistics)
"""
def normalize_building_dfs(building_dfs, method='min-max'):
    for building_name, building_df in building_dfs.items():
        if method == 'min-max':
            building_df = (building_df - building_df.min()) / (building_df.max() - building_df.min())
        elif method == 'standard-score':
            building_df = (building_df - building_df.mean()) / building_df.std()
        else:
            raise ValueError('Unknown normalization method')
        building_dfs[building_name] = building_df
    return building_dfs

if __name__ == "__main__":
    # load meters data
    meters_data = load_meters_data(esave_path)
    print(meters_data, meters_data.shape)
    print(meters_data.iloc[0])
    
    # plot test building
    building_dfs = load_and_prepare_building_dfs()
    test_building = list(building_dfs.keys())[0]
    test_building_df = building_dfs[test_building]
    test_building_df.plot()
    plt.show()

    # plot test et curve
    et_curve_dfs = load_and_prepare_et_curve_dfs()
    test_building = list(et_curve_dfs.keys())[0]
    test_fra = list(et_curve_dfs[test_building].keys())[-1]
    test_et_curve = et_curve_dfs[test_building][test_fra]
    test_et_curve.plot()
    plt.show()