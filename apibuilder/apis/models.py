from django.db import models

# Create your models here.

levels = (
    ('1','Primary'),
    ('2','Lower Secondary'),
    ('3','Secondary'),
    ('4','+2'),
    ('5','Bachelors'),
    ('6','Masters'),
    ('7','PHD'),
)


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    middle_name = models.CharField(max_length=40,blank=True)

    address = models.CharField(max_length=40)
    dob = models.DateField()
    level = models.CharField(max_length=20,choices=levels)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
