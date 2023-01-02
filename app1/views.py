from django.shortcuts import render

# Create your views here.


def ikka(request):
    return render(request, 'ikka.html')
