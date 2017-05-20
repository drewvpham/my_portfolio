from django.shortcuts import render, HttpResponse

def index(request):
    print ('mic test. 1. 2. 3')
    return render(request, 'my_portfolio/index.html')


def testimonials(request):
    print ('testimonies!')
    return render(request, 'my_portfolio/testimonials.html')
