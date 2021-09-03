import yfinance as yf
import pandas as pd
from datetime import datetime, date

from dateutil.relativedelta import *
from django.core.management.base import BaseCommand, CommandError
from stocks_background.recommendationHelper import filter_companies
from stocks_background.recommendationHelper import update_companies


class Command(BaseCommand):
    help = 'Update Recommendations'

    def handle(self, *args, **options):
        self.get_momentum()
        return


    def get_momentum(self, step=6, size=15):
        end_date = datetime.today().strftime('%Y-%m-10')
        ibov = self.get_companies()
        start_date = self.get_reference_date(end_date, step)
        prices = self.retrieve_results(ibov, start_date)
        recommendation = self.df_dict(prices, size)
        update_companies(recommendation, end_date)
        return


    def get_companies(self):
        companies = filter_companies()
        companies = [c + '.SA' for c in companies]
        return ' '.join(companies)


    def get_reference_date(self, end_date, step):
        end_date = self.convert_date_to_string(end_date)
        return end_date - relativedelta(months=step)


    def convert_date_to_string(self, dt):
        dt = dt.split('-')
        dt = [int(d) for d in dt]
        return date(dt[0],dt[1],dt[2])


    def retrieve_results(self, companies, dt):
        d = dt.strftime('%Y-%m-%d')
        result = yf.download(companies, start=d)['Close']
        return self.filter_dates(result)


    def filter_dates(self, df):
        first = self.get_row(df, 'ascending')
        last = self.get_row(df, 'descending')
        filtered = pd.concat([first, last], axis=1)
        return self.evaluate_result(filtered)


    def get_row(self, df, direction):
        is_ascending = direction == 'ascending'
        c = 1 if is_ascending else -1
        while not df.iloc[c].any():
            c = c+1 if is_ascending else c-1
        return df.iloc[c]


    def evaluate_result(self, df):
        df['growth'] = (df.iloc[:,1] - df.iloc[:,0]) / df.iloc[:,0]
        return self.parse_data(df)


    def parse_data(self, df):
        df = df.iloc[:,1:]
        df.columns = ['price', 'growth']
        return df.sort_values(by='growth', ascending=False)


    def df_dict(self, df, limit):
        df = df.head(limit)
        df = df.reset_index()
        df = df.rename({'index': 'code'}, axis=1)
        return df.to_dict(orient='records')
