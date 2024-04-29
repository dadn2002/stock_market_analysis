import yfinance as yf
import pandas as pd
import plotly.graph_objs as go


name_paper = "PETR3.SA"

try:
    # data = yf.download("PETR3.SA", start="2024-01-01", end="2024-04-04")
    # data = yf.download("PETR3.SA", period='10d')
    
    # multi_data = yf.download(["PETR3.SA", "PETR4.SA"], start="2020-01-01", end="2021-01-01")
    # print(multi_data)
    
    data1 = yf.download(name_paper, start="2024-04-18", end="2024-04-19", interval='1m', auto_adjust=True)
    data2 = yf.download(name_paper, start="2024-04-17", end="2024-04-18", interval='1m', auto_adjust=True)
    # print(data['Close'])  # This will show the adjusted close prices

    pd.set_option('display.max_rows', None)
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    # ticket = yf.Ticker("PETR3.SA")
    if data1.empty:
        print("No data available for the specified ticker symbol or date range.")
    else:
        """ 
        return value as format

        [*********************100%%**********************]  1 of 1 completed
                 Open       High        Low      Close  Adj Close    Volume
        Date
        2024-01-02  39.000000  39.630001  39.000000  39.360001  39.360001   6743900
        2024-01-03  39.380001  40.919998  39.340000  40.700001  40.700001   9800500
        2024-01-04  40.790001  41.279999  40.040001  40.040001  40.040001  10680600
        2024-01-05  40.290001  40.720001  39.980000  40.389999  40.389999   6858500
        2024-01-08  39.799999  39.990002  39.009998  39.639999  39.639999   9800700
        """
        # print(df1)
        # print(ticket.info)
        fig1 = go.Figure(data=[go.Candlestick(x=data1.index,
                                     open=data1['Open'],
                                     high=data1['High'],
                                     low=data1['Low'],
                                     close=data1['Close'])])

        fig1.show()
        pass
except Exception as e:
    print("Failed to download data:", e)
