import yfinance as yf
import pandas as pd

START_DATE = '2019-10-01'
END_DATE = '2019-11-30'
NASDAQ_TREASURY_DATA_CSV_URL = \
    "https://data.nasdaq.com/api/v3/datasets/USTREASURY/YIELD.csv?api_key=x6ZcYtB4RzvAVop7E-U6"

# We have chosen below ETFS
# Vanguard FTSE Europe Index Fund ETF Shares (VGK)
#   https://finance.yahoo.com/quote/vgk/
# SPDR Gold Shares (GLD)
#   https://finance.yahoo.com/quote/GLD/
SPDR_GOLD_ETF = 'GLD'
VOODOO_FTSE_ETF = 'VGK'

# 10 Years treasury data, so filter using START_DATE and END_DATE
treasury_yield_df_10yr = pd.read_csv(NASDAQ_TREASURY_DATA_CSV_URL, header=0, parse_dates=[0],
                                     infer_datetime_format=True)
# treasury_yield_df = treasury_yield_df_10yr.loc[START_DATE:END_DATE]
treasury_yield_df = treasury_yield_df_10yr.loc[
    (treasury_yield_df_10yr.Date >= START_DATE) & (treasury_yield_df_10yr.Date <= END_DATE)]

# Yahoo returns last day of Sept as well, so filter using START_DATE and END_DATE
gold_etf_df = yf.download(
    [SPDR_GOLD_ETF], start=START_DATE, end=END_DATE).loc[START_DATE:END_DATE]
ftse_etf_df = yf.download([VOODOO_FTSE_ETF], start=START_DATE, end=END_DATE).loc[
              START_DATE:END_DATE]

# 2.1	Compute the daily returns of your Gold ETF
gold_etf_df['Daily_returns'] = gold_etf_df['Open'] - gold_etf_df['Close']
# 2.1	Compute the daily returns of your Gold ETF
ftse_etf_df['Daily_returns'] = ftse_etf_df['Open'] - ftse_etf_df['Close']


def calculate_monthly_avg_price(df, col_name, month):
    monthly_average = df[col_name].groupby(
        df.index.map(lambda x: x.month)).mean()
    return monthly_average[month]


def calculate_monthly_avg_yield(df, col_name, month):
    monthly_average = df[col_name].groupby(
        df.Date.map(lambda x: x.month)).mean()
    return monthly_average[month]


# 3.1 to 3.3
# calculate avg yield/price of bonds and ETFs for Oct19 and Nov19
calculate_monthly_avg_yield(treasury_yield_df, '2 YR', 10)
calculate_monthly_avg_yield(treasury_yield_df, '3 YR', 10)
calculate_monthly_avg_yield(treasury_yield_df, '5 YR', 10)
calculate_monthly_avg_yield(treasury_yield_df, '7 YR', 10)
calculate_monthly_avg_yield(treasury_yield_df, '10 YR', 10)
calculate_monthly_avg_yield(treasury_yield_df, '30 YR', 10)
calculate_monthly_avg_price(gold_etf_df, 'Close', 10)
calculate_monthly_avg_price(ftse_etf_df, 'Close', 10)

calculate_monthly_avg_yield(treasury_yield_df, '2 YR', 11)
calculate_monthly_avg_yield(treasury_yield_df, '3 YR', 11)
calculate_monthly_avg_yield(treasury_yield_df, '5 YR', 11)
calculate_monthly_avg_yield(treasury_yield_df, '7 YR', 11)
calculate_monthly_avg_yield(treasury_yield_df, '10 YR', 11)
calculate_monthly_avg_yield(treasury_yield_df, '30 YR', 11)
calculate_monthly_avg_price(gold_etf_df, 'Close', 11)
calculate_monthly_avg_price(ftse_etf_df, 'Close', 11)


def calculate_std_deviation_in_price(df, col_name, month):
    monthly_average = df[col_name].groupby(
        df.index.map(lambda x: x.month)).std()
    return monthly_average[month]


def calculate_std_deviation_in_yield(df, col_name, month):
    monthly_average = df[col_name].groupby(
        df.Date.map(lambda x: x.month)).std()
    return monthly_average[month]


# 3.4 to 3.6
# calculate  std deviation in yield/price of bonds and ETFs for Oct19 and Nov19
calculate_std_deviation_in_yield(treasury_yield_df, '2 YR', 10)
calculate_std_deviation_in_yield(treasury_yield_df, '3 YR', 10)
calculate_std_deviation_in_yield(treasury_yield_df, '5 YR', 10)
calculate_std_deviation_in_yield(treasury_yield_df, '7 YR', 10)
calculate_std_deviation_in_yield(treasury_yield_df, '10 YR', 10)
calculate_std_deviation_in_yield(treasury_yield_df, '30 YR', 10)
calculate_std_deviation_in_price(gold_etf_df, 'Close', 10)
calculate_std_deviation_in_price(ftse_etf_df, 'Close', 10)


calculate_std_deviation_in_yield(treasury_yield_df, '2 YR', 11)
calculate_std_deviation_in_yield(treasury_yield_df, '3 YR', 11)
calculate_std_deviation_in_yield(treasury_yield_df, '5 YR', 11)
calculate_std_deviation_in_yield(treasury_yield_df, '7 YR', 11)
calculate_std_deviation_in_yield(treasury_yield_df, '10 YR', 11)
calculate_std_deviation_in_yield(treasury_yield_df, '30 YR', 11)
calculate_std_deviation_in_price(gold_etf_df, 'Close', 11)
calculate_std_deviation_in_price(ftse_etf_df, 'Close', 11)


pass
