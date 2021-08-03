from .models import StockRecommendations
from .models import IbovespaCompanies


def filter_companies():
    companies = IbovespaCompanies.objects.all()
    return [c.code for c in companies]


def update_companies(recommendations, reference_date):
    for r in recommendations:
        rec = StockRecommendations(
            code=r['code'], 
            value=r['value'], 
            growth=r['growth'], 
            month=reference_date
        )
        rec.save()
    return
