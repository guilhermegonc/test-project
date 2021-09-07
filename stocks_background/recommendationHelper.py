from .models import StockRecommendations,\
                    IbovespaCompanies


def filter_companies():
    companies = IbovespaCompanies.objects.all()
    return [c.code for c in companies]


def update_companies(recommendations, reference_date):
    for r in recommendations:
        rec = StockRecommendations(
            code=r['code'], 
            value=r['price'],
            active= True,
            growth=r['growth'], 
            month=reference_date
        )
        rec.save()
    return


def get_recommendations(only_actives=[True]):
    reference = StockRecommendations.objects.latest('month')
    stocks = StockRecommendations.objects.filter(month=reference.month)
    stocks = stocks.filter(active__in=only_actives).order_by('-growth')
    return [parse_recommendations(s) for s in stocks]


def parse_recommendations(stock):
    stock.code = stock.code[:-3]
    return stock

def update_status(code, status):
    new_status = status == 'true'
    code += '.SA'
    reference = StockRecommendations.objects.latest('month')
    stk = StockRecommendations.objects.get(month=reference.month, code=code)
    stk.active = new_status
    return stk.save()