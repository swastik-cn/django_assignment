from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=1000)
    user_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.name
# class Mentor(models.Model):
#     name = models.CharField(max_length=1000)
#     user_id = models.AutoField(primary_key=True)
# class Project(models.Model):
#     name = models.CharField(max_length=1000)
#     project_id = models.AutoField(primary_key=True)
# class ProjectMentor(models.Model):
#     project_id = 