# from yahooquery import Ticker
# import pandas as pd
# import numpy as np
# from datetime import datetime, date
# from dateutil.relativedelta import *

# ibov = ['ABEV3.SA','ASAI3.SA','AZUL4.SA','BTOW3.SA','B3SA3.SA','BIDI11.SA',
#         'BBSE3.SA','BRML3.SA','BBDC3.SA','BBDC4.SA','BRAP4.SA','BBAS3.SA',
#         'BRKM5.SA','BRFS3.SA','BPAC11.SA','CRFB3.SA','CCRO3.SA','CMIG4.SA',
#         'HGTX3.SA','CIEL3.SA','COGN3.SA','CPLE6.SA','CSAN3.SA','CPFE3.SA',
#         'CVCB3.SA','CYRE3.SA','ECOR3.SA','ELET3.SA','ELET6.SA','EMBR3.SA',
#         'ENBR3.SA','ENGI11.SA','ENEV3.SA','EGIE3.SA','EQTL3.SA','EZTC3.SA',
#         'FLRY3.SA','GGBR4.SA','GOAU4.SA','GOLL4.SA','NTCO3.SA','HAPV3.SA',
#         'HYPE3.SA','IGTA3.SA','GNDI3.SA','IRBR3.SA','ITSA4.SA','ITUB4.SA',
#         'JBSS3.SA','JHSF3.SA','KLBN11.SA','RENT3.SA','LCAM3.SA','LWSA3.SA',
#         'LAME4.SA','LREN3.SA','MGLU3.SA','MRFG3.SA','BEEF3.SA','MRVE3.SA',
#         'MULT3.SA','PCAR3.SA','PETR3.SA','PETR4.SA','BRDT3.SA','PRIO3.SA',
#         'QUAL3.SA','RADL3.SA','RAIL3.SA','SBSP3.SA','SANB11.SA','CSNA3.SA',
#         'SULA11.SA','SUZB3.SA','TAEE11.SA','VIVT3.SA','TIMS3.SA','TOTS3.SA',
#         'UGPA3.SA','USIM5.SA','VALE3.SA','VVAR3.SA','WEGE3.SA','YDUQ3.SA']


# def get_momentum(companies=ibov, end_date='2021-01-04', step=6):
#   dt = end_date.split('-')
#   dt = [int(d) for d in dt]
#   dt = date(dt[0], dt[1], dt[2])
  
#   results = retrieve_results(companies)
#   results = compare(results, dt, step)
#   return parse_to_json(results)

# def retrieve_results(ibovespa_companies):
#   result = Ticker(ibovespa_companies).history(period='max').reset_index()
#   return result.rename({'symbol': 'company'}, axis=1)

# def compare(results, reference_date, step):
#   past = filter_base_result(results, reference_date, step)
#   actual = filter_end_date_result(results, reference_date)
#   comparison = pd.merge(past[['company', 'past_date', 'past_price']], actual[['company', 'date', 'actual_price']], on='company')
#   comparison['growth'] = comparison['actual_price'] / comparison['past_price'] - 1
#   return comparison.sort_values(by='growth', ascending=False)

# def filter_base_result(results, reference_date, step):
#   base = results.loc[results['date'] == set_date(reference_date, step)]
#   return base.rename({'date': 'past_date', 'close': 'past_price'}, axis=1)

# def filter_end_date_result(results, reference_date):
#   actual = results.loc[results['date'] == set_date(reference_date)]
#   return actual.rename({'close': 'actual_price'}, axis=1)

# def set_date(reference, step=0):
#   date = reference - relativedelta(months=step)
#   return closest_weekday(date)

# def closest_weekday(date):
#   skip_weekend = 0 if date.weekday() < 5 else date.weekday() - 4
#   return date - relativedelta(days=skip_weekend)

# def parse_to_json(df):
#   response = {'stocks': []}
#   for _ in range(20):
#     r = df[['company', 'actual_price']].iloc[_].to_dict()
#     response['stocks'].append(r)
#   return response
