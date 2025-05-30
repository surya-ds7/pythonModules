""" matplotlib template for plotting
Use this only for reference and pick necessary code.

API Reference: https://matplotlib.org/stable/api/index.html
It is very well documented with 100s of examples

Some useful references
List of the markers available natively: https://matplotlib.org/stable/api/markers_api.html
List of the colors available natively: https://matplotlib.org/stable/gallery/color/named_colors.html
List of the colormaps available natively: https://matplotlib.org/stable/gallery/color/colormap_reference.html

Will keep updating this template code!

Other info:
For plotting -> matplotlib, seaborn, plotly are the most popular libraries and have lots of community support.
They even go hand in hand and support elements from one another.
"""
## Importing the necessary libraries and modules
## numpy is a linear algebra and math processing tools library
import matplotlib.pyplot as plot
import  matplotlib, numpy

## rcParams -> Runtime configuration parameters
## A set of default parameters load once the matplotlib is imported.
## Once changed, these will be set until they are changed again or the program ends

## Used for turning the LaTeX processing ON or OFF
matplotlib.rcParams['text.usetex'] = False

## Sets the font size of all the labels such as axis labels, 
## figure labels, text in legend, annotations, etc. to the specific font size
matplotlib.rcParams["font.size"] = 14                   # Font of the text
matplotlib.rcParams['ytick.labelsize'] = 12             # y-axis ticklabels' size
matplotlib.rcParams['xtick.labelsize'] = 12             # x-axis ticklabels' size

#####################################################
## This part is to create the data to plot
## Sine wave from 0 to (8*pi) made of points 
x = numpy.arange(0, 4*2*numpy.pi, 0.3)
y1 = numpy.abs(numpy.sin(0.28*x))
y2 = numpy.abs(numpy.cos(0.14*x))
y3 = numpy.abs((1/28) * x[::2])
#####################################################


## fig is an object which represents the canvas on which axes can be placed
## everything that needs to be displayed goes on top of the figure
fig = plot.figure(figsize=(10,6))         # values passed to the figsize are in inches representing width, height respectively.

## axes object has 2 or 3 axes (i.e. the x-axis, the y-axis, the z-axis)
## For obtaining the 3rd axis, pass projection='3d' option in the parameters to the plot
ax = fig.add_subplot(1,1,1)                     # (1,1,1) represents 1 row and 1 column and plot 1 of these.


plt1, = ax.plot(x, y1, linewidth=2, linestyle='-', marker='', color='red', label="|sin(x)|")
plt2, = ax.plot(x[::2], y2[::2], linestyle='--', marker='o', linewidth=1, markersize=10, markerfacecolor='red', label="|cos(x)|", alpha=0.5)
plt3, = ax.plot(x[::2], y3, linestyle='-', marker='s', linewidth=2, markersize=6, markerfacecolor='yellow', label="")

## To set various properties of the axis such as its title, labels, x-axis and y-axis limits, etc.
ax.set(
    ## Comment out any line whose default settings are to be unaltered
    title="Test",                                   # To set the title of the plot
    xlabel="time",                                  # To set the x-axis label
    ylabel="signal value",                          # To set the y-axis label
    xticks=[4*i for i in range(8)],             # To set the x-tick marks
    yticks=[0.0, 0.5, 1.0],                     # To set the y-tick marks
    xlim=(-1, 27),                              # To set from which x1 to what x2 the plot x-axis should be displayed
    ylim=(-0.1, 1.1),                           # To set from which y1 to what y2 the plot y-axis should be displayed
)

## To set the parameters of the ticks displayed on the axis
ax.tick_params(axis="x",direction="in", length=2,bottom=True, top=True, left=True, right=True)
ax.tick_params(axis="y",direction="in", length=2,bottom=True, top=True, left=True, right=True)


## Adding the legend and describing what lineplots to handle on the ax object
ax.legend(handles=[plt1, plt2], loc='upper right')

## To normalize the size of the total figure such that it fits inside the window
fig.tight_layout(h_pad=0.05, w_pad=0.05)

## To save a figure into a particular file type. Here it is .eps format (Encapsulated PostScript)
## Always close the figure after saving it. Otherwise it stays on memory as long as the program is running
# plot.savefig('test.eps', bbox_inches='tight', format='eps')
# plot.close('all')

## Either save the figure or show it. It is recommended (although not mandatory)
plot.show()
