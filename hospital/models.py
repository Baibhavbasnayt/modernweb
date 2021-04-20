from django.db import models
from django.utils import timezone


class Doctor(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    picture = models.ImageField(upload_to="experts/")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "hospital_doctor"


class Department(models.Model):
    name = models.CharField(max_length=120)
    pictures = models.ImageField(upload_to="department/")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "hospital_department"


class Appointment(models.Model):
    time_choices = (
        ('morning', "Morning"),
        ('evening', "Evening")
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    # doctor = models.ForeignKey(
    #     Doctor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField(default=timezone.now)
    time = models.CharField(choices=time_choices, max_length=10)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.doctor.name}"


class Admin(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "hospital_admin"

