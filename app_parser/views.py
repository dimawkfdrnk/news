from django.shortcuts import render
from .models import News, ExchangeRates
from django.shortcuts import redirect


def update_data(request):
    News.update_news()
    ExchangeRates.update_rates()
    return redirect(request.META['HTTP_REFERER'])

