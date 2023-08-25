from django.db import models

# Create your models here.

class Task(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Due_Date = models.DateTimeField()
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return self.Title
    