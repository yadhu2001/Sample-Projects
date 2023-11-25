from django.shortcuts import render
from . forms import Todoform
from .models import Todo

# Create your views here.

def index(request):
    context={}

    todo_form=Todoform()
    todo=Todo.objects.all()

    context['todo_form']=todo_form
    context['todo']=todo

    return render(request,'index.html',context)