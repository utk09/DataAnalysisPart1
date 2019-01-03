import matplotlib.pyplot as plt

prog_lang = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')

performance = [10, 8, 4, 6, 2, 12]

# Bar graph
plt.bar(prog_lang, performance, align='center', alpha=0.5)

# plt.xticks(prog_lang)

'''
ticks : array_like
A list of positions at which ticks should be placed. You can pass an empty list to disable xticks.
'''

plt.ylabel('Usage')
plt.title('Programming Language Usage')

# show plot
plt.show()
