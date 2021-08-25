from django.shortcuts import render
from app.facebookConversionAPIHelper import fb_view_content



def tic_tac_toe(request):
    fb_view_content(request)
    return render(request, 'tic-tac-toe.html')
