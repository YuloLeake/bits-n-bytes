"""
Retrieve stock data using Yahoo Finance API.
API query based on StackOverflow answer https://stackoverflow.com/a/47505102.
"""
import requests
from typing import NamedTuple

__base_url  = 'https://query1.finance.yahoo.com'
__stock_api = '/v8/finance/chart'


def fetch_historical_stock_price(
    ticker: str,
    start: int = 0,
    end: int = 9999999999,
    interval: str = '3mo'
) -> dict:
    """ Fetch historical stock prices for given ticker. """

    url = f'{__base_url}{__stock_api}/{ticker}'
    params = {
        'period1': start,
        'period2': end,
        'interval': interval
    }
    response = requests.get(url=url, params=params)

    result = response.json()['chart']['result'][0]
    timestamp  = result['timestamp']
    start_time = timestamp[0]
    end_time   = timestamp[-1]

    chart = result['indicators']['quote'][0]
    volume       = chart['volume']
    close_values = chart['close']
    high_values  = chart['high']
    low_values   = chart['low']
    open_values  = chart['open']

    fields = ['timestamp','volume','close','open','high','low']
    data = {
        'url': response.url,
        'ticker': ticker,
        'range_start': start_time,
        'range_end': end_time,
        'interval': interval,
        'data': [ dict(zip(fields, a))
                  for a 
                  in zip(timestamp, volume, close_values, open_values, high_values, low_values)]
    }

    return data

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()

    ap.add_argument('-t', '--ticker', required=True, help='Ticker symbol.')
    ap.add_argument('-s', '--start', required=False, help='Start time.')
    ap.add_argument('-e', '--end', required=False, help='End time.')
    ap.add_argument('-i', '--interval', required=False, default='3mo', help='Granularity of the historical price data.')

    args = ap.parse_args()

    print(args)

    ticker = args.ticker
    start  = 946684800
    end    = 9999999999
    interval = args.interval
    
    data = fetch_historical_stock_price(ticker, start=start, end=end, interval=interval)

    print('----------------------------------')
    print(data)
    print('')
    print(data['url'])