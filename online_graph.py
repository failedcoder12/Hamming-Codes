# Get this figure: fig = py.get_figure("https://plot.ly/~DivyanshVerma/0/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~DivyanshVerma/0/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="grouped-bar", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~DivyanshVerma/0/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('DivyanshVerma', 'kl9OVfY286DrLx2GbF6Y')
trace1 = {
  "x": ["2 bit error", "3 bit error", "4 bit error"], 
  "y": [1.85714285714, 2.2, 1.94285714286], 
  "name": "Standard Decoding", 
  "type": "bar", 
  "xsrc": "DivyanshVerma:1:492432", 
  "ysrc": "DivyanshVerma:1:e28158"
}
trace2 = {
  "x": ["2 bit error", "3 bit error", "4 bit error"], 
  "y": [1.71428571429, 2.17142857143, 1.82857142857], 
  "name": "Standard Decoding with Optimization", 
  "type": "bar", 
  "xsrc": "DivyanshVerma:1:492432", 
  "ysrc": "DivyanshVerma:1:d42af8"
}
data = Data([trace1, trace2])
layout = {"barmode": "group"}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)