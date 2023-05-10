from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import ToDoList, ToDoStep

def getToDo(request):
    toDoList = ToDoList.objects.all()
    toDoStep = ToDoStep.objects.all()
    
    context = {
        'toDoList': toDoList,
        'toDoStep': toDoStep
    }
    
    return render(request, 'toDoList.html', context)


from django.middleware.csrf import get_token

def createToDoList(request):
    if request.method == 'POST':
        # CSRF tokenını al
        csrf_token = get_token(request)
        
        # Formdan gönderilen verileri al
        id = request.POST.get('id')
        name = request.POST.get('name')
        completedPercent = request.POST.get('completedPercent', False)
        
        # ToDoStep modelinden yeni bir nesne oluştur
        toDoListData = ToDoList(id=id, name=name, completedPercent=completedPercent)
        toDoListData.save()  # Yeni nesneyi veritabanına kaydet
        
        # Listeleme sayfasına yönlendir
        return render(request, 'index.html')
    
    else:
        # CSRF tokenını al
        csrf_token = get_token(request)
        
        context = {'csrf_token': csrf_token}
        return render(request, 'index.html', context)

