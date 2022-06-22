from django.shortcuts import redirect, render
from django.http import HttpResponse
from core.form import ToDoForm
from core.models import ToDo
# from todo.core.form import ToDoForm

# Create your views here.
def home(request):
    #  creating an object 
    obj_form=ToDoForm()
    #getting values from table
    todos=ToDo.objects.all()
# getting value to db
    if request.method=='POST':
        obj_form=ToDoForm(request.POST)
        if obj_form.is_valid():
            obj_form.save()
    return render(request,'home.html',{'form':obj_form,'display':todos})

def update(request,todo_id):
    todo=ToDo.objects.get(id=todo_id)
    form=ToDoForm(instance=todo)
    if request.method=='':
        form=ToDoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form})

def delete(request,todo_id):
    data=ToDo.objects.get(id=todo_id)
    data.delete()
    return redirect('/')
  
