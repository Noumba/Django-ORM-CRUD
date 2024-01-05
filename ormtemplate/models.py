from django.db import models

# Test Model
class TestModel(models.Model):
    name = models.CharField(max_length=50),
    dob = models.CharField(max_length=50),
    
class SchoolModel(models.Model):
    schoolname = models.CharField(max_length=50),
    standard = models.CharField(max_length=50),
    

