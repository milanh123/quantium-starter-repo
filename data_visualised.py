from dash import Dash, html, dcc

import plotly.express as px
import pandas as pd

sales_data = pd.read_csv("formatted_output.csv")
sales_data["Date"] = pd.to_datetime(sales_data["Date"])

sales_data = sales_data.sort_values("Date")

figure = px.line(sales_data, x="Date", y="Sales", title="Sales Over Time by Region")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales of Pink Morsels Over Time"),

    dcc.Graph(figure=figure)
])

if __name__ == "__main__":
    app.run(debug=True)