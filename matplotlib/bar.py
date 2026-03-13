import matplotlib.pyplot as plt

# bar diagram
x = ["A", "B", "C", "D", "E"]
y = [2, 3, 4, 5, 6]

plt.bar(x, y, color= 'red')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()