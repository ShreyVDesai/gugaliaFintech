import yfinance as yf
import pandas as pd
import plotly.graph_objects as go


def get_graph():
    sid = "VIPIND.NS"
    df = yf.download(tickers=sid, interval="1m", period="1d")
    df.reset_index(inplace=True)
    df["Datetime"] = df["Datetime"].dt.tz_convert("Asia/Kolkata").dt.tz_localize(None)
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df = df.set_index("Datetime")
    df = df.tail(70)
    trace = go.Candlestick(x=df.index.strftime('%Y-%m-%dT%H:%M:%SZ').tolist(),open=df["Open"].tolist(),high=df["High"].tolist(),low=df["Low"].tolist(),close=df["Close"].tolist(),name="sid",)
    
    data = [trace]

    layout = {"title": sid}
    fig = dict(data=data, layout=layout)
    return go.Figure(fig).to_dict()

def stock_candlestick(stock):
    stock = yf.Ticker(stock)
    data = stock.history(period="100d")
    data.to_csv('yahoo.csv')

    df = pd.read_csv('yahoo.csv')
    candlestick = go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])
    fig = go.Figure(data=[candlestick])
    fig.show()

if __name__ == '__main__':
    print(get_graph())