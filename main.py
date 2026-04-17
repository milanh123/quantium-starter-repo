import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load the data
sales_data = pd.read_csv("formatted_output.csv")

# Convert Date column to datetime and sort
sales_data["Date"] = pd.to_datetime(sales_data["Date"])
sales_data = sales_data.sort_values("Date")

# Create app
app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f8",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif",
    },
    children=[
        html.Div(
            style={
                "maxWidth": "1000px",
                "margin": "0 auto",
                "backgroundColor": "white",
                "padding": "30px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.1)",
            },
            children=[
                html.H1(
                    "Pink Morsels Sales Dashboard",
                    style={
                        "textAlign": "center",
                        "color": "#2c3e50",
                        "marginBottom": "10px",
                    },
                ),
                html.P(
                    "Use the radio buttons below to filter sales by region.",
                    style={
                        "textAlign": "center",
                        "color": "#555",
                        "marginBottom": "25px",
                    },
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={
                        "textAlign": "center",
                        "marginBottom": "30px",
                    },
                    inputStyle={"marginRight": "6px", "marginLeft": "12px"},
                ),
                dcc.Graph(id="sales-line-chart"),
            ],
        )
    ],
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_data = sales_data.copy()
    else:
        filtered_data = sales_data[
            sales_data["Region"].str.lower() == selected_region
        ].copy()

    figure = px.line(
        filtered_data,
        x="Date",
        y="Sales",
        title=f"Sales Over Time - {selected_region.title()}",
        labels={"Date": "Date", "Sales": "Sales"},
    )

    figure.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#2c3e50"),
        title_x=0.5,
    )

    return figure


if __name__ == "__main__":
    app.run(debug=True)