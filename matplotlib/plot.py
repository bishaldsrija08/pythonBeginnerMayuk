import matplotlib.pyplot as plt

# plotting

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x,y, 'o-.r',ms = 20)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot of y = x^2')
plt.show()  