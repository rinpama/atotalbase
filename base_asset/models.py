from django.db import models

class Document(models.Model):
    title=models.CharField('ﾀｲﾄﾙ', max_length=50,null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True,)
    upload = models.FileField(upload_to='document/',default='')