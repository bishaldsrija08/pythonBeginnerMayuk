import matplotlib.pyplot as plt

# pie chart

x = [10, 20, 30, 40]
mylabels = ["A", "B", "C", "D"]
myexplode = [0, 0.2, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(x, labels=mylabels, explode=myexplode, shadow=True, colors=mycolors)
plt.legend(title="Here are the labels")
plt.show()