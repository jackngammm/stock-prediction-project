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









