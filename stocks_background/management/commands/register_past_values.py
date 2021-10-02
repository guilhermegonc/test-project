from dateutil.relativedelta import *
from django.core.management.base import BaseCommand, CommandError

from stocks.models import StockValues
from stocks.stocksHelper import get_companies_in_wallets

import yfinance as yf
import pandas as pd
from datetime import datetime

import sys

class Command(BaseCommand):
    help = 'Update Stock Values'
    def handle(self, *args, **options):
        self.get_values()
        return


    def get_values(self):
        wallet = self.list_companies()
        return self.retrieve_results(wallet)


    def list_companies(self):
        companies = get_companies_in_wallets()
        companies = [c['code'] + '.SA' for c in companies]
        return ' '.join(companies)


    def retrieve_results(self, companies):
        start, end = self.filter_dates()
        try:
            company_values = yf.download(companies, start=start, end=end)['Close'].reset_index()
            company_values = self.parse_yf(company_values, start)
            return self.parse_stocks(company_values, start) if company_values.shape[0] > 0 else None
        except:
            return


    def filter_dates(self):
        end = datetime.today()
        start = end - relativedelta(days=1)
        return start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d')

    def parse_yf(self, stock_data, reference_date):
        stock_data = stock_data.loc[stock_data['Date'] == reference_date]
        stocks = stock_data.drop('Date', axis=1).iloc[0]
        if stocks.sum() == 0:
            return
        return stock_data.drop('Date', axis=1).iloc[0]

    def parse_stocks(self, companies, reference_date):
        companies = companies.to_dict()
        results = [self.save_stock_value(c, v, reference_date) for c, v in companies.items()]
        return results

    
    def save_stock_value(self, company, value, dt):
        stock = StockValues(
            code = company[:-3],
            value = value,
            reference_date = dt
        )
        stock.save()
        return stock
