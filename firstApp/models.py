from django.db import models

# Create your models here.

class Student(models.Model):
    class Gender(models.TextChoices):
        Male= 'M', 'male'
        Female = 'F', 'Female'

    gender = models.CharField(max_length=7, choices=Gender.choices , default=Gender.Male)
    # GENDER_CHOICES = (
    #     ('male', 'male'),	
    #     ('female', 'female'),
    # )
    # gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
