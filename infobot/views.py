from django.shortcuts import render
from .models import MyModel

def my_model_view(request):
    my_models = MyModel.objects.all()
    return render(request, 'my_model.html', {'my_models': my_models})
