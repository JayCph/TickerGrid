import yfinance as yf

stock = yf.Ticker("GOOGL")
stock.info
stock.analyst_price_targets

def fetch_ticker_data(symbol: str) -> dict:
