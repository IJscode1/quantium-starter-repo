import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

df = pd.read_csv("formatted_output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = Dash(__name__)

COLORS = {
    "background": "#fdf2f8",
    "card": "#ffffff",
    "primary": "#e91e63",
    "text": "#333333",
    "muted": "#666666"
}

app.layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": COLORS["background"],
        "minHeight": "100vh",
        "padding": "40px"
    },
    children=[
        html.Div(
            style={
                "backgroundColor": COLORS["card"],
                "borderRadius": "12px",
                "padding": "30px",
                "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.08)",
                "maxWidth": "1100px",
                "margin": "0 auto"
            },
            children=[
                html.H1(
                    "Soul Foods, Pink Morsel Sales Visualiser",
                    style={
                        "textAlign": "center",
                        "color": COLORS["primary"],
                        "marginBottom": "10px"
                    }
                ),
                html.P(
                    "Were sales higher before or after the price increase on 15 January 2021?",
                    style={
                        "textAlign": "center",
                        "fontSize": "18px",
                        "color": COLORS["muted"],
                        "marginBottom": "30px"
                    }
                ),
                html.Div(
                    style={
                        "textAlign": "center",
                        "marginBottom": "20px",
                        "padding": "15px",
                        "backgroundColor": COLORS["background"],
                        "borderRadius": "8px"
                    },
                    children=[
                        html.Label(
                            "Filter by region:",
                            style={
                                "fontWeight": "bold",
                                "marginRight": "15px",
                                "color": COLORS["text"]
                            }
                        ),
                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                                {"label": "All", "value": "all"}
                            ],
                            value="all",
                            inline=True,
                            style={"display": "inline-block"},
                            inputStyle={"marginLeft": "15px", "marginRight": "5px"}
                        )
                    ]
                ),
                dcc.Graph(id="sales-chart")
            ]
        )
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.title()})",
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
        hovermode="x unified",
        plot_bgcolor="#fafafa"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)