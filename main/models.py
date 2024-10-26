from django.db import models
from users.models import User

# Create your models here.
class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.datetime)[0:10] +" "+ str(self.student.username)