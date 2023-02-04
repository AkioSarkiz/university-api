from django.db import models
from django.contrib.auth.models import AbstractUser


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    # more fields here

    def __str__(self):
        return f"{self.username}"


class StudentGroup(TimestampModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return "Group {}".format(self.name)


class Student(TimestampModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)


class Teacher(TimestampModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
