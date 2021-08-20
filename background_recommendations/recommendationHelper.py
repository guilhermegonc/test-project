from .models import StockRecommendations
from .models import IbovespaCompanies

import sys

def filter_companies():
    companies = IbovespaCompanies.objects.all()
    return [c.code for c in companies]


def update_companies(recommendations, reference_date):
    for r in recommendations:
        rec = StockRecommendations(
            code=r['code'], 
            value=r['price'], 
            growth=r['growth'], 
            month=reference_date
        )
        rec.save()
    return


def get_recommendations():
    reference = StockRecommendations.objects.latest('month')
    print(reference.month)
    sys.stdout.flush()
    recommendations = StockRecommendations.objects.filter(month=reference.month)
    return recommendations
