import matplotlib.pyplot as plt

# line diagram
x = [1, 5, 3, 1, 2]
y = [2, 3, 4, 5, 6]

plt.plot(x, ls = ':', color = 'r', linewidth = '20.5')
plt.plot(y, ls = '--', color = 'g', linewidth = '10.5')
plt.grid()
plt.show()