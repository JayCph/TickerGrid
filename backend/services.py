import yfinance as yf


def fetch_ticker_data(symbol: str):
    stock = yf.Ticker(symbol)

    raw_data = stock.info

    processed_data = {
        "price": raw_data.get("regularMarketPrice", 0.0),
        "currency": raw_data.get("currency", ""),
        "previous_close": raw_data.get("regularMarketPreviousClose", 0.0),
        "dividend_yield": raw_data.get("dividendYield", 0.0),
    }

    return processed_data


# Aktuelt printer vi dette til terminalen, men vi kan også returnere det til frontenden efter den er sat op
if __name__ == "__main__":
    test_symbol = "SPKSJF.CO"
    print(f"Fetching data for {test_symbol}...")
    print(fetch_ticker_data(test_symbol))
