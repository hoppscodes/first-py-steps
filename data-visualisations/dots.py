import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
#s=200 is the size of the point.
ax.scatter(2, 4, s=200)

ax.set_title("squares", fontsize=24)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("square values uwu", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
