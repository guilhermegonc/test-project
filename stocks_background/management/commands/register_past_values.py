import yfinance as yf
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import *
from django.core.management.base import BaseCommand, CommandError

from stocks.models import StockValues
from stocks.stocksHelper import get_companies_in_wallets

import sys

class Command(BaseCommand):
    help = 'Update Stock Values'

    def handle(self, *args, **options):
        self.get_values()
        return


    def get_values(self):
        wallet = self.get_companies_in_wallet()
        return self.retrieve_results(wallet)


    def get_companies_in_wallet(self):
        companies = get_companies_in_wallets()
        companies = [c['code'] + '.SA' for c in companies]
        return ' '.join(companies)


    def retrieve_results(self, companies):
        start, end = self.filter_dates()
        try:
            company_values = yf.download(companies, start='2021-08-23', end='2021-08-24')['Close'].iloc[0]
            return self.parse_stocks(company_values)
        except:
            pass


    def filter_dates(self):
        end = datetime.today()
        start = end - relativedelta(days=1)
        return start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d')


    def parse_stocks(self, companies):
        companies = companies.to_dict()
        results = [self.save_stock_value(c, v) for c, v in companies.items()]
        return results

    
    def save_stock_value(self, company, value):
        stock = StockValues(
            code = company[:-3],
            value = value,
            reference_date = date.today() - relativedelta(days=1)
        )
        stock.save()
        return stock
