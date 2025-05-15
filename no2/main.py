from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Stock API"}

@app.get("/stocks/{symbol}")
def get_stock_data(symbol: str):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="5d")
    data = hist["Close"].to_dict()
    return {"symbol": symbol.upper(), "close": data}

