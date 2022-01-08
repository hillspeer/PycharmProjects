#Import modules
import plotly
import plotly.graph_objs as go

#Make Plotly figure
from plotly import data

fig1 = go.Scatter(x=data['curb-weight'],
                  y=data['price'],
                  mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(xaxis=dict(title="curb-weight"),
                     yaxis=dict( title="price"))

#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True)