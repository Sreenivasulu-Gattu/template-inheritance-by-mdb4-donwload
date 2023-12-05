from django.shortcuts import render

# Create your views here.
def parent(request):
    return render(request,'index.html')


def child1(request):
    return render(request,'child1.html')