from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

fig = Figure()
canvas = FigureCanvas(fig)
x = np.random.randn(10000)

ax = fig.add_subplot(111)
#111 is convention for one row, one column, and uses the first cell in that grid for the location of the new axes
ax.hist(x,100)
#100bins
ax.set_title("Normal distribution")
#fig.savefig("matplotlib_histogram.png")

plt.hist(x, 100)
plt.title("normal distribution with $\mu = 0 ,\sigma = 1$")
plt.show()







