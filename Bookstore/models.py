from django.db import models

# Create your models here.
class BookModel(models.Model):    
    unique_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200, null = False, blank = False)
    author_name = models.CharField(max_length = 200)
    cost = models.DecimalField(decimal_places = 2, max_digits = 6)
    publication_year = models.PositiveIntegerField()
    pages = models.IntegerField(null = True, blank = True)

def __str__(self):
    return self.name