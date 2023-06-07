from django.urls import path
from . import views

app_name = 'file_upload'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
]
