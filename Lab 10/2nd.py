import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]
y3 = [5, 10, 15, 20, 25]

plt.plot(x, y1, label="y = 2x", marker='o')
plt.plot(x, y2, label="y = x²", marker='s')
plt.plot(x, y3, label="y = 5x", marker='^')

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Multiple Line Graph Example")
plt.legend()
plt.show()
