import fileinput

import numpy
import plotly

dataSet = []
xData = []

sunspotData = open("sunspots.txt")
for line in sunspotData:
    i+= 1

line = sunspotData.readlines()
for j in range (i-24,i+1):
    xData[count] = line[j]

x = dataSet[:,0]
xplot = (x/12)+1749
y = dataSet[:,1]

trace0= plotly.graph_objs.Scatter(x = xplot,y = y,mode = 'lines+markers')

data = [trace0]

layout = dict(title = 'Sunspot data since 1749',xaxis = dict(title = 'Year'),yaxis = dict(title = 'Number of Sunspots'))
fig = dict(data = data, layout = layout)
plotly.offline.plot(fig, filename = "Sunspots Graph.html")
