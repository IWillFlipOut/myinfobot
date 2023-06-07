from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import MyModel
from .forms import DocumentForm

def my_model_view(request):
    my_models = MyModel.objects.all()
    return render(request, 'my_model.html', {'my_models': my_models})

def handle_uploaded_file(f):
    with open('infobot/files/' + str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'infobot/upload.html', {
        'form': form
    })