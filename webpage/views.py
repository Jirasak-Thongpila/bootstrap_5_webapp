from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def for_view(request):
    context = {}
    context['message'] = "การวนซ้ำใน_Django"

    if request.method == 'POST' and request.POST.get('count') != '':
        number = int(request.POST.get('count'))
        context['count'] = list(range(1,number +1))
    else:
        context['count'] = list(range(1, 2))

    return render(request, 'for.html',context)

def multipli(request):
    context = {}
    context['message'] = "ตารางสูตรคูณ"

    if request.method == 'POST' and request.POST.get('number') != '':
        number = int(request.POST.get('number'))
        context['number'] = number
        context['table'] = [(i, number * i) for i in range(1, 13)]
    else:
        context['table'] = []
        context['number'] = None

    return render(request, 'table.html', context)

def student(request):
    contaxt = {}
    contaxt['title'] = "รายชื่อนักศึกษา"

    students = models.Student.objects.all()
    contaxt['students'] = students

    return render(request, 'Student.html', contaxt)

def subjects(request):
    contaxt = {}
    contaxt['title'] = "รายวิชา"

    subjects = models.Subjects.objects.all()
    contaxt['subjects'] = subjects

    return render(request, 'Subject.html', contaxt)
