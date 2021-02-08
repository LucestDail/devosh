from django.shortcuts import render

# Create your views here.


def portfolio_main(request):
    return render(request, 'portfolio_main.html')