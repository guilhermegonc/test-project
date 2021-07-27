import yfinance as yf
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import *


from .recommendationHelper import filter_companies
from .recommendationHelper import update_companies


import sys

def get_momentum(step=6, size=15):
    end_date=datetime.today().strftime('%Y-%m-10')
    ibov = get_companies()
    start_date = get_reference_date(end_date, step)
    prices = retrieve_results(ibov, start_date)
    return
    recommendation = df_dict(prices, size)
    update_companies(recommendation, end_date)
    return recommendation


def get_companies():
    companies = filter_companies()
    companies = [c + '.SA' for c in companies]
    return ' '.join(companies)


def get_reference_date(end_date, step):
    end_date = convert_date_to_string(end_date)
    return end_date - relativedelta(months=step)


def convert_date_to_string(dt):
    dt = dt.split('-')
    dt = [int(d) for d in dt]
    return date(dt[0],dt[1],dt[2])


def retrieve_results(companies, dt):
    d = dt.strftime('%Y-%m-%d')
    result = yf.download(companies, start=d)['Close']
    print(result)
    sys.stdout.flush()
    return filter_dates(result)


def filter_dates(df):
    first = get_row(df, 'ascending')
    last = get_row(df, 'descending')
    filtered = pd.concat([first, last], axis=1)
    return evaluate_result(filtered)


def get_row(df, direction):
    is_ascending = direction == 'ascending'
    c = 1 if is_ascending else -1
    while not df.iloc[c].any():
        c = c+1 if is_ascending else c-1
    return df.iloc[c]


def evaluate_result(df):
    df['growth'] = (df.iloc[:,1] - df.iloc[:,0]) / df.iloc[:,0]
    return parse_data(df)


def parse_data(df):
    df = df.iloc[:,1:]
    df.columns = ['price', 'growth']
    return df.sort_values(by='growth', ascending=False)


def df_dict(df, limit):
    df = df.head(limit)
    df = df.reset_index()
    df = df.rename({'index': 'code'}, axis=1)
    return df.to_dict(orient='records')
