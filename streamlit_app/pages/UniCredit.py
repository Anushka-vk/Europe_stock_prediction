import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

st.set_page_config(page_title="UniCredit Stock Prediction")

st.markdown("<h1 style='text-align: center;'><em>UniCredit STOCK EXCHANGE</em></h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'><u>UniCredit</u></h2>", unsafe_allow_html=True)

df = pd.read_csv("../STREAMLIT_APP/EuropeFGIS2.csv",parse_dates=['Date'], index_col='Date')  # Load stock data
x = df[df["Symbol"] == "UniCredit"].copy()
x = x.drop('Symbol', axis=1)

# Pre-processing
x = x[['Close']].dropna()
x['Returns'] = x['Close'].pct_change()

def check_stationarity(timeseries):
    result = adfuller(timeseries.dropna())
    if result[1] > 0.05:
        x['Close_Diff'] = x['Close'].diff().dropna()

model = ARIMA(x['Close'], order=(6,1,0))
model_fit = model.fit()

forecast = model_fit.forecast(steps=10)
dates = pd.date_range(start=x.index[-1], periods=11, freq='B')[1:]

fig = go.Figure()
fig.add_trace(go.Scatter(x=x.index, y=x['Close'], mode='lines', name='Actual Prices'))
fig.add_trace(go.Scatter(x=dates, y=forecast, mode='lines', name='Predicted Prices', 
                         line=dict(dash='dot', color='red')))

fig.update_layout(title="UniCredit Stock Price Prediction",
                  xaxis_title='Date', yaxis_title='Stock Price',
                  template="plotly_white", legend=dict(x=0, y=1))

st.plotly_chart(fig, use_container_width=True)

st.markdown("<h3 style='text-align: center;'>Predicted Stocks for next 10 Days</h3>", unsafe_allow_html=True)

predict_df = pd.DataFrame({'Date': dates, 'Price': forecast}).reset_index().drop('index', axis=1)
st.table(predict_df)

if st.button("Back to Home"):
    st.switch_page("app.py")  # ✅ Now correctly points to home