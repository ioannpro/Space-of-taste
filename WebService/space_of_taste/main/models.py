from django.db import models



class File(models.Model):
     url=models.TextField(blank=True)
class Category(models.Model):
    name=models.CharField(max_length=320)
    icons=models.TextField()
class Dish(models.Model):
    object=None
    name=models.CharField(max_length=320,verbose_name='Имя')
    image=models.ForeignKey('File',on_delete=models.CASCADE)
    categori=models.ForeignKey('Category',on_delete=models.CASCADE)
    description=models.TextField(blank=True)
    options=models.JSONField()



