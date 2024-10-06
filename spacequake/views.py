# views.py
from django.shortcuts import render, redirect
from .models import MyModel
from .forms import MyModelForm  # Make sure to create this form

def mymodel_create_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page or index
    else:
        form = MyModelForm()
    return render(request, 'mymodel_form.html', {'form': form})

def home(request):
    return render(request, 'home.html')  # This will render the 'home.html' template
