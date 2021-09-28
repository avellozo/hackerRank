'''from sklearn import linear_model
import numpy as np
xl = [1, 2, 3, 4, 5]
x = np.asarray(xl).reshape(-1, 1)
y = [2, 1, 4, 3, 5]
lm = linear_model.LinearRegression()
lm.fit(x, y)
print(lm.intercept_)
print(lm.coef_[0])'''

import statistics as st


def Pearson(X, Y):
    ret = 0

    for i in range(n):
        ret += (X[i] - m_x) * (Y[i] - m_y)

    return (ret / (std_x * std_y * n))


X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

std_x = st.pstdev(X)
std_y = st.pstdev(Y)
m_x = st.mean(X)
m_y = st.mean(Y)
n = len(X)

b = Pearson(X, Y)*std_y/std_x
a = m_y - b*m_x

print(round(a+b*80, 3))
