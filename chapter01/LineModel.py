# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split


def loan_data():
    diabetes = datasets.load_diabetes()
    data = train_test_split(diabetes.data, diabetes.target, test_size=0.25, random_state=0)
    return data


def test_LinearRegression(*data):
    X_train, X_test, y_train, y_test = data
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    print('Coefficients:%s,intercept %.2f' % (regr.coef_, regr.intercept_))
    print("Residual sum of squares:%.2f" % np.mean((regr.predict(X_test) - y_test) ** 2))
    print('Score:%.2f' % regr.score(X_test, y_test))


def test_Ridge(*data):
    X_train, X_test, y_train, y_test = data
    regr = linear_model.Ridge()
    regr.fit(X_train, y_train)
    print('Coefficients:%s,intercept %.2f' % (regr.coef_, regr.intercept_))
    print("Residual sum of squares:%.2f" % np.mean((regr.predict(X_test) - y_test) ** 2))
    print('Score:%.2f' % regr.score(X_test, y_test))


def test_Ridge_alpha(*data):
    X_train, X_test, y_train, y_test = data
    alphas = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    scores = []
    for i, alpha in enumerate(alphas):
        regr = linear_model.Ridge(alpha=alpha)
        regr.fit(X_train, y_train)
        scores.append(regr.score(X_test, y_test))

    # 绘图
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(alphas, scores)
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel(r"score")
    ax.set_xscale('log')
    ax.set_title("Ridge")
    plt.show()


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = loan_data()
    # test_LinearRegression(X_train, X_test, y_train, y_test)
    # test_Ridge(X_train, X_test, y_train, y_test)
    test_Ridge_alpha(X_train, X_test, y_train, y_test)
