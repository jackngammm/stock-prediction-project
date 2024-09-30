from data_getter import fetch_stock_data
from plotter import plot_graph,plot_predictions
from prediction import predict_future_prices


if __name__ == "__name__":
     stock_symbol = input("Enter the stock symbol (e.g., AAPL, TSLA): ")
     start_date = input("Enter the start date (YYYY-MM-DD): ")
     end_date = input("Enter the end date (YYYY-MM-DD): ")

     stock_data = fetch_stock_data(stock_symbol, start_date, end_date)

     if (stock_data is not None and not stock_data.empty):
          plot_graph(stock_data, stock_symbol)
          future_days = int(input("Enter the number of days you want to predict: "))
          future_predict, future_x = predict_future_prices(stock_data, future_days)

          for i, price in enumerate(future_predict, start = 1):
               print(f"Day {i}: {price:.2f} USD")

          plot_predictions(stock_data, future_x, future_predict, stock_symbol, future_days)

     else:
          print("No data available for the selected data range.")