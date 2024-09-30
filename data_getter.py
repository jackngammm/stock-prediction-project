import yfinance as yf
from datetime import datetime, timedelta


def fetch_stock_data(stock_symbol, start_date, end_date):
    try:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format! Please enter the date in 'YYYY-MM-DD'")
        return None
    

    if start > end:
        print("Start date cannot be later than end date.")
        return None
    
    stock_Data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_Data

stock_symbol = input("Enter the stock symbol (e.g., AAPL, TSLA): ")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

stock_data = fetch_stock_data(stock_symbol, start_date, end_date)

if stock_data is not None:
    print(stock_data)