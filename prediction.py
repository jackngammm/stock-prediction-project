import numpy as np
from sklearn.linear_model import LinearRegression

def predict_future_prices(stock_data, future_days):
    stock_data['Days'] = np.arange(1, len(stock_data) + 1)
    x = stock_data['Days']
    y = stock_data['Close']

    model = LinearRegression()
    model.fit(x,y)
    
    #predict future prices
    future_x =  np.arange(len(stock_data) + 1, len(stock_data) + future_days + 1).reshape(-1,1)
    future_predict = model.predict(future_x)

    return future_predict, future_x