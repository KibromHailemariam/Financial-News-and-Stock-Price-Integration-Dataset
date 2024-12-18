import pandas as pd
import talib

def calculate_indicators(df):
    df['SMA'] = talib.SMA(df['close'], timeperiod=14)
    df['EMA'] = talib.EMA(df['close'], timeperiod=14)
    df['RSI'] = talib.RSI(df['close'], timeperiod=14)
    df['MACD'], df['MACD_signal'], _ = talib.MACD(df['close'])
    return df

df = pd.read_csv('task_2/data/processed_data.csv')
df_with_indicators = calculate_indicators(df)
df_with_indicators.to_csv('task_2/data/indicators_data.csv', index=False)