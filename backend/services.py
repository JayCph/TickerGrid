from typing import TypedDict, cast

import yfinance as yf  # pyright: ignore[reportMissingTypeStubs]


class TickerData(TypedDict):
    price: float
    currency: str
    previous_close: float
    dividend_yield: float


def fetch_ticker_data(symbol: str) -> TickerData:
    stock = yf.Ticker(symbol)

    raw_data = cast(dict[str, float | str | None], stock.info)

    processed_data: TickerData = {
        "price": float(raw_data.get("currentPrice") or 0.0),
        "currency": str(raw_data.get("currency") or "USD"),
        "previous_close": float(raw_data.get("regularMarketPreviousClose") or 0.0),
        "dividend_yield": float(raw_data.get("dividendYield") or 0.0)
    }

    return processed_data


# Aktuelt printer vi dette til terminalen, men vi kan også returnere det til frontenden efter den er sat op
if __name__ == "__main__":
    test_symbol = "SPKSJF.CO"
    print(f"Fetching data for {test_symbol}...")
    print(fetch_ticker_data(test_symbol))
