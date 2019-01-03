import matplotlib.pyplot as plt

# some random values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Labelling X-axis, Y-axis and Title
plt.xlabel('x-list')
plt.ylabel('y-list')
plt.title('Relation Between Squares')

# Plotting the graph
plt.plot(x, y)
plt.show()
