import fileinput

import numpy
import plotly

dataSet = []

#sunspotData = fileinput.input("sunspots.txt",float)
#for line in sunspotData:
    #dataSet.append()

dataSet =numpy.loadtxt("sunspots.txt",float)

x = dataSet[:,0]
xplot = (x/12)+1749
y = dataSet[:,1]

trace0= plotly.graph_objs.Scatter(x = xplot,y = y,mode = 'lines+markers')

data = [trace0]

layout = dict(title = 'Sunspot data since 1749',xaxis = dict(title = 'Year'),yaxis = dict(title = 'Number of Sunspots'))
fig = dict(data = data, layout = layout)
plotly.offline.plot(fig, filename = "Sunspots Graph.html")
