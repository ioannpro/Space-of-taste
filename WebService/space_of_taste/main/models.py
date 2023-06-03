from django.db import models

class Dish(models.Model):
    object=None
    name=models.CharField(max_length=320,verbose_name='Имя')
    image=models.ForeignKey('File')
    categori=models.ForeignKey('Category')
    description=models.TextField(blank=True)
    options=models.JSONField()
    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=320)
    upcategory=models.SmallIntegerField()
    icons=models.ForeignKey('File')

class File(models.Model):
    url=models.TextField(blank=True)






