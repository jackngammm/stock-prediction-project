import matplotlib.pyplot as plt


def plot_graph(stock_data, stock_symbol):

    if stock_data is not None and not stock_data.empty:
        plt.figure(figsize=(10,5))
        plt.plot(stock_data.index, stock_data['Close'], label = 'Closing Price', market='o')
        plt.title(f'{stock_symbol} Stock Price ({stock_data.index.min().date()} to {stock_data.index.max().date()})')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print(f"No data avaialble for {stock_symbol} in the selected date range.")





def plot_predictions(stock_data, future_x, future_predict, stock_symbol, future_days):
    if stock_data is not None and not stock_data.empty:
        plt.figure(figsize=(10,5))
        plt.plot(stock_data.index, stock_data['Close'], label = 'Historical Price', market='o')
        plt.plot(future_x, future_predict, label=f'Predicted Prices ({future_days} days)', linestyle = '--')
        plt.title(f'{stock_symbol} Stock Price Prediction (Next{future_days} Days)')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print(f"No data avaialble for {stock_symbol} in the selected date range.")




