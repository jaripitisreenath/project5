from django.shortcuts import render

# Create your views here.
def sree(request):
    d={'name':'sreenath','age':22}
    return render(request,'sree.html',d)