"""
Retrieve stock data using Yahoo Finance API.
Based on StackOverflow answer https://stackoverflow.com/a/47505102.

"""
import requests

__base_url = 'https://query1.finance.yahoo.com'
__stock_api = '/v8/finance/chart'

def fetch_stock_price(
    ticker: str,
    start: int = 0,
    end: int = 9999999999,
    interval: str = '3mo'
):
    """ """

    url = f'{__base_url}{__stock_api}/{ticker}'
    params = {
        'period1': start,
        'period2': end,
        'interval': interval
    }
    response= requests.get(url=url, params=params)

    print(response.text)
    print('')
    print(response.url)


if __name__ == '__main__':
    import argparse

    ap = argparse.ArgumentParser()

    ap.add_argument('-t', '--ticker', required=True, help='Ticker symbol.')
    ap.add_argument('-s', '--start', required=False, help='Start time.')
    ap.add_argument('-e', '--end', required=False, help='End time.')

    args = ap.parse_args()

    print(args)

    ticker = args.ticker
    start  = 946684800
    end    = 9999999999

    interval = '3mo'
    
    fetch_stock_price(ticker, start=start, end=end, interval=interval)