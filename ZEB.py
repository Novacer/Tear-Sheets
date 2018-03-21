import pandas as pd
import pyfolio as pf


prices = pd.read_csv('ZEB Historical Data.csv')
benchmark = pd.read_csv('SP TSX Canadian Financials Historical Data.csv')

prices = prices[::-1]
benchmark = benchmark[::-1]

prices['Date'] = pd.to_datetime(prices.Date)
prices.set_index('Date', inplace=True)

benchmark['Date'] = pd.to_datetime(benchmark.Date)
benchmark.set_index('Date', inplace=True)

change = prices['Change %'].div(100)
bench_change = benchmark['Change %'].div(100)

change.dropna(inplace=True)
bench_change.dropna(inplace=True)
print(change)

print(change.shape)
print(bench_change.shape)

# notice to user! rolling fama french has been disabled!!!!!
pf.tears.create_returns_tear_sheet(change, benchmark_rets=bench_change)
