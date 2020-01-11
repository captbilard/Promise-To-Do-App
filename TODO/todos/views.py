from django.shortcuts import render, redirect
from .forms import TodoForm
from django.views import View, generic
from django.shortcuts import get_object_or_404
from .models import Todo
# Create your views here.


class AddTodoView(View):
    form_class = TodoForm
    template_name = "todo/index.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        todos = Todo.objects.all()
        return render(request, self.template_name, {'form':form, 'todos':todos})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-todo')
        return render(request, self.template_name, {'form':form})

def completed(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('add-todo')

def deleteCompleted(request):
    Todo.objects.get(completed__exact=True).delete()
    return redirect('add-todo')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('add-todo')