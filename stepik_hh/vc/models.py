from django.db import models

# Create your models here.


class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    specty = models.CharField(max_length=60)


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.PositiveIntegerField()


class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=60)
    description = models.TextField()
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateTimeField()
