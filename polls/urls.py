from django.urls import path
from .views import send_data, upload_resume

urlpatterns = [
    path('send-data/', send_data, name='send_data'),
    path('resume/', upload_resume, name='upload_resume')
]