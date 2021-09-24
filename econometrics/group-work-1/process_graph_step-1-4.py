import requests
import csv
import yfinance as yf
import pandas as pd

START_DATE = '2019-10-01'
END_DATE = '2019-11-30'
NASDAQ_TREASURY_DATA_CSV_URL = "https://data.nasdaq.com/api/v3/datasets/USTREASURY/YIELD.csv?api_key=x6ZcYtB4RzvAVop7E-U6"

# We have choosen below ETFS
# Vanguard FTSE Europe Index Fund ETF Shares (VGK)
#   https://finance.yahoo.com/quote/vgk/
# SPDR Gold Shares (GLD)
#   https://finance.yahoo.com/quote/GLD/
SPDR_GOLD_ETF = 'GLD'
VOODOO_FTSE_ETF = 'VGK'

# 10 Years treasury data, so filter using START_DATE and END_DATE
treasury_csv_data = pd.read_csv(NASDAQ_TREASURY_DATA_CSV_URL, header=0, parse_dates=[
    0], infer_datetime_format=True).loc[START_DATE:END_DATE]

# Yahoo returns last day of Sept as well, so filter using START_DATE and END_DATE
gold_etf_df = yf.download(
    [SPDR_GOLD_ETF], start=START_DATE, end=END_DATE).loc[START_DATE:END_DATE]
ftse_etf_df = yf.download([VOODOO_FTSE_ETF], start=START_DATE, end=END_DATE).loc[
    START_DATE:END_DATE]

# calculate daily returns of gold etf
gold_etf_df['Daily_returns'] = gold_etf_df['Open'] - gold_etf_df['Close']
ftse_etf_df['Daily_returns'] = ftse_etf_df['Open'] - ftse_etf_df['Close']


def calculate_monthly_avg(df, col_name, month):
    monthly_avg = df[col_name].groupby(
        gold_etf_df.index.map(lambda x: x.month)).mean()
    return monthly_avg[month]


# avg gold returns for the month Oct and Nov 2019
monthly_gold_etf_avg = gold_etf_df['Close'].groupby(
    gold_etf_df.index.map(lambda x: x.month)).mean()

# avg FTSE returns for the month Oct and Nov 2019
monthly_ftse_etf_avg = ftse_etf_df['Close'].groupby(
    ftse_etf_df.index.map(lambda x: x.month)).mean()

pass
