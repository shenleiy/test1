import matplotlib.pyplot as plt


y_squares = list(range(1, 1000))
x_squares = [x ** 2 for x in y_squares]

plt.scatter(x_squares, y_squares, s=10)
plt.axis([0, 1100000, 0, 1100])
plt.show()
