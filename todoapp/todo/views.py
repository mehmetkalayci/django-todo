from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    items = TodoItem.objects.all()
    return render(request, 'todo.html',
                  {'items': items}
                  )


def addTodo(request):
    newItem = TodoItem(content=request.POST['content'])
    newItem.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, item_id):
    item2delete = TodoItem.objects.get(id=item_id)
    item2delete.delete()
    return HttpResponseRedirect('/todo/')