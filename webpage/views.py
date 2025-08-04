from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def for_view(request):
    context = {}
    context['count'] = list(range(1, 11)) 
    context['message'] = "การวนซ้ำใน_Django"
    return render(request, 'for.html',context)