import requests
import csv
import yfinance as yf
import pandas as pd

start_date = '2019-10-01'
end_date = '2019-11-30'


US_TREASURY_10Y = '^TNX'
# download via yahoo finance
#us_treasury_10y_df = yf.download([US_TREASURY_10Y], start=start_date, end=end_date)

# download from treasury.gov in the XML format
# wget "http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=year(NEW_DATE)%20eq%202019"

# download from nasdaq using the API in csv format
NASDAQ_TREASURY_DATA_CSV_URL = "https://data.nasdaq.com/api/v3/datasets/USTREASURY/YIELD.csv?api_key=x6ZcYtB4RzvAVop7E-U6"

treasury_csv_data = []
with requests.get(NASDAQ_TREASURY_DATA_CSV_URL, stream=True) as r:
    lines = (line.decode('utf-8') for line in r.iter_lines())
    for row in csv.reader(lines):
        # print(row)
        treasury_csv_data.append(row)
        pass

treasury_csv_data = pd.read_csv(NASDAQ_TREASURY_DATA_CSV_URL, header=0, parse_dates=[
                                0], infer_datetime_format=True)
SPDR_GOLD_ETF = 'GLD'
VOODOO_FTSE_ETF = 'VGK'

gold_etf_df = yf.download([SPDR_GOLD_ETF], start=start_date, end=end_date)
ftse_etf_df = yf.download([VOODOO_FTSE_ETF], start=start_date, end=end_date)


pass
