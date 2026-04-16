import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

df = pd.read_csv("formatted_output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = Dash(__name__)

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales ($)"}
)

fig.add_shape(
    type="line",
    x0="2021-01-15", x1="2021-01-15",
    y0=0, y1=1,
    yref="paper",
    line=dict(color="red", width=2, dash="dash")
)

fig.add_annotation(
    x="2021-01-15",
    y=1,
    yref="paper",
    text="Price Increase (15 Jan 2021)",
    showarrow=False,
    yshift=10,
    font=dict(color="red")
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales ($)",
    hovermode="x unified"
)

app.layout = html.Div(
    style={"fontFamily": "Arial, sans-serif", "margin": "40px"},
    children=[
        html.H1(
            "Soul Foods, Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#e91e63"}
        ),
        html.P(
            "Were sales higher before or after the price increase on 15 January 2021?",
            style={"textAlign": "center", "fontSize": "18px", "color": "#555"}
        ),
        dcc.Graph(id="sales-chart", figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)