from django.shortcuts import render,redirect
from django.contrib import messages


# import todoform and models
from .forms import TodoForm
from .models import Todo


# Create your views here.
 
def Index(request):
 
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', page)

def Remove(request,item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item Removed!!")
    return redirect('todo')
    