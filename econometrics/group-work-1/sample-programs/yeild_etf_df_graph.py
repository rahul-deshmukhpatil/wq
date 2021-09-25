# Import pandas library
import matplotlib.pyplot as plt
import pandas as pd

treasury_yield_df = pd.read_csv('treasury_yield_df.csv', header=0, parse_dates=['Date'], index_col='Date')
ftse_etf_df = pd.read_csv('ftse_etf_df.csv', header=0, parse_dates=['Date'], index_col='Date')
gold_etf_df = pd.read_csv('gold_etf_df.csv', header=0, parse_dates=['Date'], index_col='Date')

etf_prices = ftse_etf_df
etf_prices['fste_etf_price'] = ftse_etf_df['Close']
etf_prices['gold_etf_price'] = gold_etf_df['Close']

fig, ax1 = plt.subplots()
etf_prices.plot(ax=ax1, y=['fste_etf_price', 'gold_etf_price'], ylabel='gold_etf_price', secondary_y=['fste_etf_price'], grid=True)
treasury_yield_df.plot(ax=ax1, ylabel='Yields', grid=True)

# treasury_yield_df.plot(xticks=treasury_yield_df.index)
# plt.legend(loc='best')
# plt.show()


# try https://stackoverflow.com/questions/32999619/how-to-label-y-axis-when-using-a-secondary-y-axis as well

pass
