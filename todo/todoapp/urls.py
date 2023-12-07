from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo,name="main"),
    path("todo-delete<int:item_id>",views.todo_delete,name="tododelete"),
    path('clear-items/', views.clear_items, name='clear_items'),
    path('todo-edit/<int:item_id>', views.edit_todo, name='edit_todo'),
    path('todo-complete/<int:item_id>', views.todo_complete, name='complete_todo'),
]