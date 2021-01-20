from django.db import models

class Students(models.Model):
    sid = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    father = models.CharField(max_length=50)
    mother = models.CharField(max_length=50)
    email = models.EmailField()
    degree = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)

    class Meta:
        db_table = "students"
