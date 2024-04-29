from datetime import date, datetime, timedelta
import dash
from dash import dcc, html, Input, Output
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

paper_name = "PETR3.SA"

# Function to create a candlestick figure for the selected date
def create_graph(data, selected_date):
    if data is not None:
        filtered_data = data[data.index.date == selected_date]
        fig = go.Figure(data=[go.Candlestick(x=filtered_data.index,
                                              open=filtered_data['Open'], high=filtered_data['High'],
                                              low=filtered_data['Low'], close=filtered_data['Close'])])
        fig.update_layout(
            title=f"Stock Data for {selected_date}",
            margin=dict(l=10, r=10, t=30, b=10),
            xaxis_rangeslider_visible=False,
            height=300,  # Smaller graph height
            width=800    # Smaller graph width
        )
        return dcc.Graph(figure=fig)
    else:
        return html.Div("No data available for the selected date.")


# Download data and create the Dash app  
def download_data(paper_name):
    try:
        return yf.download(paper_name, period='60d', interval='5m')
    except Exception as e:
        print(f"Failed to download data: {e}")
        return None


# Calculate the last 7 days (including today)
today = datetime.today()
last_seven_days = [today - timedelta(days=i) for i in range(7)]

# Filter out weekends (Saturday and Sunday)
last_seven_weekdays = [day for day in last_seven_days if day.weekday() < 5]

# Set the minimum and maximum dates allowed in the date picker
min_date_allowed = min(last_seven_weekdays)
max_date_allowed = max(last_seven_weekdays)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Daily Stock Price Visualization', style={'text-align': 'center'}),
    html.Div([
        html.Label('Enter Stock Symbol:'),
        dcc.Input(
            id='paper_input',
            type='text',
            value='PETR3.SA',  # Default value
            style={'width': '200px', 'margin': '0 auto', 'display': 'block'}  # Center the input field
        ),
    ], style={'text-align': 'center'}),
    html.Div([
        html.H2('Sale Date Select', style={'text-align': 'center'}),
        dcc.DatePickerSingle(
            id='sale_date_picker',
            # min_date_allowed=min_date_allowed,
            # max_date_allowed=max_date_allowed,
            date=max_date_allowed,  # Default to the most recent weekday
            initial_visible_month=max_date_allowed,
            style={'width': '200px', 'margin': '0 auto', 'display': 'block'},  # Center the date picker
        ),
    ], style={'padding': '20px', 'text-align': 'center'}),
    html.Div(id='selected_date_graph', style={'padding': '20px', 'text-align': 'center', 'display': 'flex', 'justify-content': 'center'}),
])


# Callback to update the graph based on the selected date and paper name
@app.callback(
    Output('selected_date_graph', 'children'),
    [Input('paper_input', 'value'),
     Input('sale_date_picker', 'date')]
)
def update_graph(paper_name, selected_date):
    # data = download_data(paper_name)
    if selected_date is not None and data is not None:
        selected_date = pd.to_datetime(selected_date).date()
        return create_graph(data, selected_date)
    else:
        return None


if __name__ == '__main__':
    data = download_data(paper_name)
    app.run_server(debug=True)
