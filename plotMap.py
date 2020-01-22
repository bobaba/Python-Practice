import matplotlib.pyplot as plt


class PlotRoute():
  """ Show the route on a plot 
  
  initialize with a list of city points and the desired route to plot\n
  optionally, pass in the distance to show on the plot as well
  """
  def __init__(self, cities, route, title = None, xLabel = None, yLabel = None):
    xs = [cities[i][0] for i in route]
    ys = [cities[i][1] for i in route]

    fig, ax = plt.subplots()
    ax.plot(xs, ys, marker="D")
    if xLabel != None:
      ax.set_xlabel(f"{xLabel}", fontsize=15)
    if yLabel != None: 
      ax.set_ylabel(f"{yLabel}", fontsize=15)
    if title != None: 
      ax.set_title(f"{title}")

    ax.grid(True)
    fig.tight_layout()

    plt.show()

