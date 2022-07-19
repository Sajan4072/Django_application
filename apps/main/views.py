from django.shortcuts import render

# Create your views here.

def HomeView(request):
    # return render(request,'../../templates/home/index.html')
    return render(request,'home/index.html')