import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

'''
The default startangle is 0, which would start the "Frogs" slice on the positive x-axis. 
This example sets startangle = 90 such that everything is rotated counter-clockwise by 90 degrees, 
and the frog slice starts on the positive y-axis.
'''

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

'''
plt.subplots() is a function that returns a tuple containing a figure and axes object(s). 
Thus when using fig1, ax1 = plt.subplots() you unpack this tuple into the variables fig1 and ax1. 
Having fig is useful if you want to change figure-level attributes or 
save the figure as an image file later (e.g. with  fig.savefig('yourfilename.png'). 
You certainly don't have to use the returned figure object 
but many people do use it later so it's common to see. 
Also, all axes objects (the objects that have plotting methods), have a parent figure object anyway, thus:
fig1, ax1 = plt.subplots()

is more concise
'''
