from django.db import models

class ImageStore(models.Model):
    image_name=models.CharField(max_length=200)
    image=models.FileField(upload_to='ImageStore',null=False,default=None)

