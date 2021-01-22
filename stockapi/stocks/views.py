from django.shortcuts import render
from django.template import loader

#yahoo-finance api
from yahoo_finance import Share

# Create your views here.
def index(request):
    yahoo = Share('YHOO')
    print(yahoo.get_open(),yahoo.get_price(),yahoo.get_trade_datetime())
    return render(request, 'index.html')

def result(request, stock_id):
    #something something
    return render(request,'result.html',{'context':context})