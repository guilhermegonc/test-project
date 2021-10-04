from django.shortcuts import render


def tic_tac_toe(request):
    return render(request, 'tic-tac-toe.html')
