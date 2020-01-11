from django.shortcuts import render, redirect
from .forms import TodoForm
from django.views import View
# Create your views here.
class AddTodoView(View):
    form_class = TodoForm
    template_name = "todo/index.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-todo')
        return render(request, self.template_name, {'form':form})