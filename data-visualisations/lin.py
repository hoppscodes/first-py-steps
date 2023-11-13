#import the pyplot module from the matplotlib. define it as plt for future reference
import matplotlib.pyplot as plt

#define input
input_values = [1, 2, 3, 4, 5]
#define squares as values in []
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn-v0_8-dark')
#set the whole diagram up. the fig variable is the whole picture. the ax variable is one diagram. subplots is a plt function that shows one particular diagram.
fig, ax = plt.subplots()
#plot is a variable that attempts to present the data in a reasonable way in the diagram.
ax.plot(input_values, squares, linewidth=3)
#this runs the matplotlib explorer.

#define title, labels and their respective font size
ax.set_title("squares", fontsize=24)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("square values", fontsize=14)
#define label size
ax.tick_params(axis='both', labelsize=14)

plt.show()



