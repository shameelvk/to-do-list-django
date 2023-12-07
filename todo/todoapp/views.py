from django.shortcuts import render,redirect
from todoapp.models import TodoItem

# Create your views here.
def todo(request):
    if request.POST:
       value=request.POST["item"]
       new_todo=TodoItem(title=value)
       new_todo.save()
    todo_all=TodoItem.objects.all()
    return render(request,'index.html',{'data':todo_all})
def todo_delete(request,item_id):
    ob=TodoItem.objects.get(id=item_id)
    ob.delete()
    return redirect("main")


def clear_items(request):
    TodoItem.objects.all().delete()
    return redirect('main')

def edit_todo(request,item_id):
    if request.POST:
        value=request.POST['edit']
        obj=TodoItem.objects.get(id=item_id)
        obj.title=value
        obj.completed=False
        obj.save()
        return redirect("main")
    ob=TodoItem.objects.get(id=item_id)
    return render(request,'edit.html',{"data":ob})

def todo_complete(request,item_id):
    obj=TodoItem.objects.get(id=item_id)
    obj.completed=True
    obj.save()
    return redirect('main')