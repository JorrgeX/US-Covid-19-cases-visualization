#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dash components
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Graph components
import plotly.graph_objects as go
import plotly.offline as po
import plotly.express as px

# Pandas
import pandas as pd

app = dash.Dash()

df = pd.read_csv("all-states-history.csv")
# print(df)

df_sorted = df.sort_values(by="date")
df_today = df.loc[df["date"] == df_sorted["date"][0]]
# print(df_today)

figure = go.Figure(
    data = go.Choropleth(
        z = df_today["death"],
        locations = df_today["state"],
        locationmode = "USA-states",
        autocolorscale = True,
    )
)

figure.update_layout(
    title_text = "Deaths",
    geo_scope = "usa",
)

app.layout = html.Div([
    html.H1("HackPSU Covid Dashboard (US)"),
    dcc.Graph(
        id = "main_graph", 
        figure = figure, 
    ),
    dcc.Dropdown(
        id = "data_select",
        options = [{"label": col, "value": col} for col in df.columns.values[3:]]
    )
])

@app.callback(Output("main_graph", "figure"),
             [Input("data_select", "value")])
def update_fig(value):
    figure = go.Figure(
    data = go.Choropleth(
        z = df_today["death"],
        locations = df_today["state"],
        locationmode = "USA-states",
        autocolorscale = True,
    )
)
    figure.update_layout(
    title_text = value,
    geo_scope = "usa",
)
    return figure
    

if __name__ == "main":
    app.run_server()


# In[ ]:




