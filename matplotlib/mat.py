import matplotlib.pyplot as plt

print(plt.matplotlib.__version__)

# bar diagram
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.bar(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Diagram')
plt.show()