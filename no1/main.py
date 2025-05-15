import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# 저장 폴더 준비
os.makedirs("data", exist_ok = True)
os.makedirs("charts", exist_ok = True)

# S&P500 종목 목록 가져오기
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
sp500_table = pd.read_html(url)[0] # 첫 번째 테이블
TICKERS = sp500_table["Symbol"].tolist()[:100]

START_DATE = "2024-01-01"
END_DATE = datetime.today().strftime("%Y-%m-%d")

for ticker in TICKERS:
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(start = START_DATE, end = END_DATE)

        if df.empty:
            print(f"[X] {ticker} 데이터 없음")
            continue

        df.to_csv(f"data/stock_{ticker}.csv")
        print(f"[✓] {ticker} 데이터 저장 완료")
        
         # 차트 저장
        plt.figure(figsize=(10, 4))
        df["Close"].plot(title=f"{ticker} Closing Price")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.grid(True)
        plt.savefig(f"charts/stock_{ticker}_plot.png")
        plt.close()

    except Exception as e:
        print(f"[!] {ticker} 처리 중 오류 발생: {e}")
