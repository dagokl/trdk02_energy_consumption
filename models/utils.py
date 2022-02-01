import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse

df = pd.read_excel("data/EsaveExportSmall.xls")
df.rename(columns={df.columns[0]: "datetime"}, inplace=True)
datetime = df.pop("datetime")

# changes decimal separator and parses string to float
df = df.applymap(lambda cell: float(str(cell).replace(",", ".")))


# evaluates model with mse
# start is how many data points the model is given
# num_predicts is the number of predictions to make
def mse(model, start, num_predicts):
    history = df.iloc[:start, 0].values.tolist()
    expected = df.iloc[start:start + num_predicts, 0].values.tolist()

    predicted = []
    for _ in range(num_predicts):
        prediction = model.predict_next(history)
        predicted.append(prediction)
        history.append(prediction)

    mse = mean_squared_error(expected, predicted)

    plot_series(range(start + num_predicts), [history, history[:start] + expected])
    return mse


def plot_series(time, series):
    for s in series:
        plt.plot(time, s)
    plt.show()


if __name__ == '__main__':
    plot_series(range(len(datetime[:50])), [df.iloc[:50, 0], df.iloc[:50, 1], df.iloc[:50, 2]])
