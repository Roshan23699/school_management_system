from django.db import models
from django.contrib.auth.models import User, auth
# from django.core.exceptions import ValidationError
# from django.core.validators import MaxValueValidator
# from django.core.exceptions import ValidationError


# Create your models here.
class Notice(models.Model):
	marqueeHeading = models.CharField(max_length=50, default='')
	heading = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='pdf', default='')
	datePublished = models.DateTimeField()
	# offer = models.BooleanField(default=False)
	def __str__(self):
		return self.heading

class School(models.Model):
	name = models.CharField(max_length=50, default='')
	
	def __str__(self):
		return self.name

class Year(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	yearname = models.IntegerField(default=2020)
	def __str__(self):
		return str(self.yearname)
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	year = models.ForeignKey(Year, on_delete=models.CASCADE,default=2020)
	studentname = models.CharField(default='', max_length=50)
	YEAR_CHOICES = [
        (int(5), '5th'),
        (int(6), '6th'),
        (int(7), '7th'),
        (int(8), '8th'),
        (int(9), '9th'),
        (int(10), '10th'),
    ]
	standard = models.IntegerField(choices=YEAR_CHOICES,default=5)
	DIV_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F')
    ]
	divison = models.CharField(max_length=1,choices=DIV_CHOICES,default='A')
	def __str__(self):
		return self.studentname + ' (' + str(self.standard) + ' ' + self.divison + ')' 


class Result(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE,default='')
	YEAR_CHOICES = [
        (int(5), '5th'),
        (int(6), '6th'),
        (int(7), '7th'),
        (int(8), '8th'),
        (int(9), '9th'),
        (int(10), '10th'),
    ]
	standard = models.IntegerField(choices=YEAR_CHOICES,default=5)
	TERM = [
		(1, 'First'), 
		(2, 'Second'),
	]
	term = models.PositiveSmallIntegerField(choices=TERM, default=1)
	EXAM_CHOICES = [
		('unit test', 'Unit test'), 
		('semister', 'Semister')
	]
	exam = models.CharField(choices=EXAM_CHOICES,default='unit test', 
	max_length=20)
	Maximum_marks_for_each_subject = models.IntegerField(default=20)
	Marathi = models.IntegerField(default=0, blank=True, )
	Hindi = models.IntegerField(default=0, blank=True,)
	English = models.IntegerField(default=0, blank=True, )
	Mathematics = models.IntegerField(default=0, blank=True, )
	SocialScience = models.IntegerField(default=0, blank=True, )
	Science = models.IntegerField(default=0, blank=True, )
	Total_obtained_marks = models.IntegerField(default=0, blank=True, editable=False)
	Total_maximum_marks = models.IntegerField(default=0, blank=True, editable=False)
	def __str__(self):
		return str(self.standard) + ' ' + str(self.term) + ' ' + str(self.exam)
	def save(self):
		self.Total_maximum_marks = self.Maximum_marks_for_each_subject * 6
		self.Total_obtained_marks = self.Marathi + self.Mathematics + self.English + self.SocialScience + self.Science + self.Hindi
		super().save()

class Tenth_Result(models.Model):
	year_choices = [
        (2021, '2020-21'),
        (2022, '2021-22'),
        (2023, '2022-23'),
        (2024, '2023-24'),
        (2025, '2024-25'),
        (2026, '2025-26'),
        (2027, '2026-27'),
    ]
	# year = models.CharField()
	year = models.IntegerField(choices=year_choices,default=2020,unique=True) 
	heading = models.CharField(max_length=100)
	username = None
	USERNAME_FIELD = 'year'
	REQUIRED_FIELDS = [year, heading, ]
	def __str__(self):
		return self.year




class Tenth_Topper(models.Model):
	tenth_result = models.ForeignKey(Tenth_Result, on_delete=models.CASCADE)
	name = models.CharField(max_length=30, default='')
	percentage = models.SmallIntegerField(default=100)
	image= models.ImageField(upload_to='media/images', default='')



class Profile(models.Model): 
	student = models.OneToOneField(Student, on_delete=models.CASCADE)
	date_of_admission = models.DateField()
	father_name = models.CharField(max_length=40)
	mother_name = models.CharField(max_length=40)
	father_occupation = models.CharField(max_length=20)
	mother_occupation = models.CharField(max_length=20, default='')
	parent_contact_1 = models.IntegerField(default=1234567890)
	parent_contact_2 = models.IntegerField(default=1234567890)
	temporary_address = models.CharField(max_length = 100, blank = True)
	permenant_address = models.CharField(max_length = 100, blank = True)
	student_contact = models.CharField(max_length = 100, blank = True)
	image = models.ImageField(upload_to='media/images')
	def __str__(self):
		return self.student.studentname + ' profile'


class Homework(models.Model):
	YEAR_CHOICES = [
        (int(5), '5th'),
        (int(6), '6th'),
        (int(7), '7th'),
        (int(8), '8th'),
        (int(9), '9th'),
        (int(10), '10th'),
    ]
	standard = models.IntegerField(choices=YEAR_CHOICES,default=5)
	DIV_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F')
    ]
	divison = models.CharField(max_length=1,choices=DIV_CHOICES,default='A')
	subject = models.CharField(max_length=20, default='Mathematics')
	date_added = models.DateTimeField(auto_now=True)
	submission_date = models.DateField()
	heading = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	def __str__(self):
	 return str(self.standard) + '   ' + self.divison + '  (' + self.heading + ')'

	
	