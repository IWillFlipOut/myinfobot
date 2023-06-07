from django.shortcuts import render
from .forms import DocumentForm

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_upload')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})