'''
K-Nearest Neighbors (KNN) Algorithm Implementation

https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm

This script demonstrates the implementation of the K-Nearest Neighbors algorithm
from scratch for classification on the Iris dataset.

The KNN algorithm is a simple and effective supervised learning algorithm used
for classification and regression tasks. It classifies a new data point based on
the majority class of its k-nearest neighbors in the feature space.

Dataset: Iris Dataset
- Features: Sepal length, sepal width, petal length, petal width
- Classes: Setosa, Versicolor, Virginica
'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def euclidean_distance(self, x, y):
        return np.linalg.norm(x - y)

    '''
    Taking input as X_test: it is a matrix containing features of test samples.
    Running through individual points
        1. calculating euclidean's distance storing it to distances list
        2. sorting the distances list and slicing till k
        3. checking for labels existing in y_train
        4. appending the most common label to y_predicted
        5. return y_predicted
    '''
    def predict(self, X_test):
        y_predicted = []
        for test_sample in X_test:
            distances = [self.euclidean_distance(test_sample, train_point) for train_point in self.X_train]
            indices = np.argsort(distances)[:self.k]
            labels = [self.y_train[i] for i in indices]
            bincount_result = np.bincount(labels)
            prediction = np.argmax(bincount_result)
            y_predicted.append(prediction)
        return y_predicted

'''
This function is used to load the iris dataset from sklearn.datasets
Iris dataset= [data, target, target_names, feature_names]

returns:
1. X: the np matrix containing features
2. y: the list of labels
3. classes: list that contains target names
'''
def get_data():
    data = load_iris()
    X = data.data
    y = data.target
    classes = data.target_names
    return X, y, classes

def main():
    X, y, classes = get_data() 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    k = int(input('Enter the hyperparameter k: '))


    mdl = KNN(k) #intializing the KNN class, requires to set hyper paramter k, experiment with it.
    mdl.fit(X_train, y_train) 
    y_predicted = mdl.predict(X_test) #runs prediction on X_test, return a list of predicted values for test data

    target_hm= {
        0: 'setosa', 
        1: 'versicolor',
        2: 'virginica',
    } #straight away initializing hardcode list, cuz i'm lazy :)
 
    prediction= pd.DataFrame(y_test, columns= ['Actual'])
    prediction['Predicted']= y_predicted
    prediction['Actual_flowers']= prediction['Actual'].map(target_hm)
    prediction['Predicted_flowers']= prediction['Predicted'].map(target_hm)

    print(prediction)

    print("Accuracy:", accuracy_score(y_test, y_predicted)) #printing the accuracy

if __name__ == '__main__':
    main()