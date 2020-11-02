from django.db import models
from django.contrib.auth.models import User, auth
# from django.core.exceptions import ValidationError
# from django.core.validators import MaxValueValidator
# from django.core.exceptions import ValidationError


# Create your models here.
class School(models.Model):
	name = models.CharField(max_length=50, default='')
	
	def __str__(self):
		return self.name
class Year(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	yearname = models.IntegerField(default=2020)
	def __str__(self):
		return str(self.yearname)

class Notice(models.Model):
	marqueeHeading = models.CharField(max_length=50, default='')
	heading = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='pdf', default='')
	datePublished = models.DateTimeField()
	# offer = models.BooleanField(default=False)
	def __str__(self):
		return self.heading




class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	year = models.ForeignKey(Year, on_delete=models.CASCADE,default=2020)
	roll_no = models.IntegerField()
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

# CREATE TABLE `student` (
# 	`Name` varchar(30) NOT NULL,
# 	`Roll No` INT NOT NULL,
# 	`division` varchar(1) NOT NULL,
# 	`Standard` INT NOT NULL,
# 	`Email` varchar(20) NOT NULL,
# 	`Mobile` varchar(10) NOT NULL,
# 	`Address Id` varchar(5) NOT NULL,
# 	PRIMARY KEY (`Roll No`,`division`,`Standard`)
# );






class Result(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE,default='')
	marks = models.IntegerField(default=0,blank=True)
	subject_id = models.CharField(max_length=6)

# CREATE TABLE `Result` (
# 	`Roll No` INT NOT NULL,
# 	`Division` varchar(1) NOT NULL,
# 	`Standard` INT NOT NULL,
# 	`Subject Id` varchar(5) NOT NULL,
# 	`Marks` INT NOT NULL,
# 	PRIMARY KEY (`Roll No`,`Division`,`Standard`,`Subject Id`)
# );

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

class District_state(models.Model):
	district_state_id = models.CharField(max_length=5)
	district = models.CharField(max_length=10)
	state = models.CharField(max_length = 10)

class City_district(models.Model):
	city_district_id = models.CharField(max_length =5)
	city = models.CharField(max_length=10)
	district_state_id = models.ForeignKey(District_state, on_delete=models.CASCADE)

class Address(models.Model):
	address_id = models.CharField(max_length=5)
	house_no = models.CharField(max_length=10)
	area = models.CharField(max_length=10)
	street_name = models.CharField(max_length =10)
	city_district_id = models.ForeignKey(City_district, on_delete=models.CASCADE)
# CREATE TABLE `Address` (
# 	`Address Id` varchar(5) NOT NULL,
# 	`house No/Name` varchar(10) NOT NULL,
# 	`Area` varchar(10) NOT NULL,
# 	`Street Name` varchar(10) NOT NULL,
# 	`City` varchar(10) NOT NULL,
# 	`District` varchar(10) NOT NULL,
# 	`State` varchar(10) NOT NULL,
# 	PRIMARY KEY (`Address Id`)
# );

class Subject(models.Model):
	YEAR_CHOICES = [
        (int(5), '5th'),
        (int(6), '6th'),
        (int(7), '7th'),
        (int(8), '8th'),
        (int(9), '9th'),
        (int(10), '10th'),
    ]
	subject_id = models.CharField(max_length=5)
	standard = models.IntegerField(choices=YEAR_CHOICES,default=5)
	name = models.CharField(max_length=10)

# CREATE TABLE `Subject` (
# 	`Subject Id` varchar(5) NOT NULL,
# 	`Standard` INT NOT NULL,
# 	`Type` varchar(10) NOT NULL,
# 	`Subject Name` varchar(10) NOT NULL,
# 	PRIMARY KEY (`Subject Id`,`Standard`)
# );






class Profile(models.Model): 
	student = models.OneToOneField(Student, on_delete=models.CASCADE)
	date_of_admission = models.DateField()
	father_name = models.CharField(max_length=40)
	mother_name = models.CharField(max_length=40)
	father_occupation = models.CharField(max_length=20)
	mother_occupation = models.CharField(max_length=20, default='')
	parent_contact_1 = models.IntegerField(default=1234567890)
	parent_contact_2 = models.IntegerField(default=1234567890)
	# temporary_address = models.CharField(max_length = 100, blank = True)
	# permenant_address = models.CharField(max_length = 100, blank = True)
	address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
	student_contact = models.CharField(max_length = 100, blank = True)
	image = models.ImageField(upload_to='media/images', default = 'mainsite/images/passport.jpg')
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
	DIV_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F')
    ]
	assignment_no = models.IntegerField()
	standard = models.IntegerField(choices=YEAR_CHOICES,default=5)
	description = models.CharField(max_length=200)
	divison = models.CharField(max_length=1,choices=DIV_CHOICES,default='A')
	subject_id = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now=True)
	submission_date = models.DateField()
	heading = models.CharField(max_length=50)
	def __str__(self):
	 return str(self.standard) + '   ' + self.divison + '  (' + self.heading + ')'


# CREATE TABLE `Homework` (
# 	`Assignment No` INT NOT NULL,
# 	`Subject Id` varchar(5) NOT NULL,
# 	`Standard` INT NOT NULL,
# 	`Description` varchar(50) NOT NULL,
# 	`Last Date` TIMESTAMP NOT NULL,
# 	PRIMARY KEY (`Assignment No`,`Subject Id`,`Standard`)
# );
	



class Teaches(models.Model):
	YEAR_CHOICES = [
        (int(5), '5th'),
        (int(6), '6th'),
        (int(7), '7th'),
        (int(8), '8th'),
        (int(9), '9th'),
        (int(10), '10th'),
    ]
	DIV_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F')
    ]
	teacher_id= models.CharField(max_length=5)
	subject_id=models.CharField(max_length=5)
	standard = models.IntegerField(choices=YEAR_CHOICES,default=5)
	divison = models.CharField(max_length=1,choices=DIV_CHOICES,default='A')
# CREATE TABLE `Teaches` (
# 	`teacher Id` varchar(5) NOT NULL,
# 	`Subject Id` varchar(5) NOT NULL,
# 	`Standard` INT NOT NULL,
# 	`Division` varchar(1) NOT NULL,
# 	PRIMARY KEY (`teacher Id`,`Subject Id`,`Standard`,`Division`)
# );
class Teacher(models.Model):
	name = models.CharField(max_length=20)
	teacher_id = models.CharField(max_length =5)
	salary = models.IntegerField()
	email = models.EmailField()
# CREATE TABLE `Teacher` (
# 	`Name` varchar(20) NOT NULL,
# 	`Teacher Id` varchar(5) NOT NULL,
# 	`Salary` INT NOT NULL,
# 	`Email` varchar(20) NOT NULL,
# 	PRIMARY KEY (`Teacher Id`)
# );


