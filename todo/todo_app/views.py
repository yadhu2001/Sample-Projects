from django.shortcuts import render
from . forms import Todoform
from .models import Todo
 
# Create your views here.

def index(request):
    context={}
    form=Todoform()


    if request.method=='POST':
        if 'save' in request.POST:
            key=request.POST.get('save')

            if not key:
                form=Todoform(request.POST)
            else:
                print(key)
                todo_edit=Todo.objects.get(id=key)
                form=Todoform(request.POST, instance=todo_edit)


            form.save()
            form=Todoform
            
        elif 'delete' in request.POST:
            key=request.POST.get('delete')
            todo=Todo.objects.get(id=key)
            todo.delete()

        elif 'edit' in request.POST:
            key=request.POST.get('edit')
            todo_edit=Todo.objects.get(id=key)
            form=Todoform(instance=todo_edit)

    todo=Todo.objects.all


    context['form']=form
    context['todo']=todo
    return render (request,'index.html',context)