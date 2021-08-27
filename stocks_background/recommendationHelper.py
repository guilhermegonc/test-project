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
            growth=r['growth'], 
            month=reference_date
        )
        rec.save()
    return


def get_recommendations():
    reference = StockRecommendations.objects.latest('month')
    return StockRecommendations.objects.filter(month=reference.month)
