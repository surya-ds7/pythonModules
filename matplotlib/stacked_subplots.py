import matplotlib.pyplot as plt

# SMALL_SIZE = 14
# MEDIUM_SIZE = 20
# BIGGER_SIZE = 36

# plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
# plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
# plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
# plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
# plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

fig = plt.figure(figsize=(8, 6))

# Add a subplot using [left, bottom, width, height] in figure coordinates
ax1 = fig.add_axes([0.3, 0.15, 0.5, 0.5])  # lower-left subplot
ax2 = fig.add_axes([0.2, 0.35, 0.5, 0.5])  # lower-right subplot
ax3 = fig.add_axes([0.1, 0.55, 0.5, 0.5])  # top subplot

ax1.set_title("Bottom Left")
ax2.set_title("Bottom Right")
ax3.set_title("Top")

plt.show()
