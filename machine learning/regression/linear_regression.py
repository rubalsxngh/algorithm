import pandas as pd
import numpy as np
# using scikit learn to check the accuracy score of the model
from sklearn.metrics import mean_squared_error


def get_data(link='data\salary_dataset.csv'):
    df = pd.read_csv(link, index_col=0)
    return df


def linear_reg(x, y):

    x = np.array(x)
    y = np.array(y)

    lenm, lenr = x.shape[1], x.shape[0]

    X = np.column_stack((np.ones(lenr), x))

    coefficients = np.linalg.inv(X.T @ X) @ X.T @ y

    c = coefficients[0]
    m = coefficients[1:]

    y_pred = X @ coefficients

    return y_pred


def main():
    dataframe = get_data()
    cols = [col for col in dataframe.columns]

    X, y = dataframe[cols[:-1]
                     ].astype('float64'), dataframe[cols[-1]].astype('float64')
    y_pred = linear_reg(X, y)

    mse = mean_squared_error(y, y_pred)
    print(f"Mean Squared Error: {mse}")


if __name__ == "__main__":
    main()
