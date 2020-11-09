from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
​
if __name__ == '__main__':
    n_train = int(input().split()[1])
    X_train = []
    y_train = []
    for i in range(n_train):
        row = [float(x) for x in input().split()]
        X_train.append(row[:-1])
        y_train.append(row[-1])
    n_test = int(input())
    X_test = []
    for i in range(n_test):
        row = [float(x) for x in input().split()]
        X_test.append(row)
    est = Pipeline([
        ('trans', PolynomialFeatures(4)),
        ('est', LinearRegression())
    ])
    est.fit(X_train,y_train)
    y_pred = est.predict(X_test)
    for v in y_pred:
        print(v)
