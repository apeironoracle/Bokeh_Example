# Load package
import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure, show


# Set up data
M = 201
x = np.array(range(M))
y = x
source = ColumnDataSource(data=dict(x=x[0:1], y=y[0:1]))


# Set up plot
plot = figure(height=400, width=400, title="moving point",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, M], y_range=[0, M])

plot.line(x, y)


# init index
plot.circle('x', 'y', source=source, size=10)


# Set up widget
index = Slider(title="index", value=0, start=0, end=200, step=1)


# Set up callbacks
def update_data(attrname, old, new):

    # Get the current slider values
    i = index.value

    # Generate the new point
    source.data = dict(x=x[i:i+1], y=y[i:i+1])

index.on_change('value', update_data)


# Set up layouts and add to document
curdoc().add_root(column(plot, index, width=400))
curdoc().title = "Moving Point with Slider"
