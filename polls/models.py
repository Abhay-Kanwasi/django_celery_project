from django.db import models

class Resume(models.Model):
    pdf = models.FileField(upload_to='pdfs')
    photos = models.ImageField(upload_to='photos')
