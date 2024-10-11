from django.db import models






class Category(models.Model):
   title = models.CharField(max_length=40, unique=True)

   def __str__(self):
       return self.title

   class Meta:
       ordering = ['title']
       verbose_name_plural = 'categories'