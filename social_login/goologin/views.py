from django.shortcuts import render

# Create your views here.
def _index(request):
    return render(request, 'index.html')

def _detail(request):
    return render(request,'detail.html')