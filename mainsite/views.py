from django.shortcuts import render, HttpResponse, redirect
from .models import Notice
from .models import Student, Year
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from .models import Homework, Student, Result
from django.shortcuts import get_object_or_404
from django.db.models import Max
from django.http import JsonResponse
from django.urls import reverse



# Create your views here.
def index(request):
	
	if request.user.is_authenticated: 
		return redirect('personalInfo')
	print('hello')
	notices = Notice.objects.all()
	parameters = {'notices' : notices}
	return render(request, 'mainsite/index.html', parameters)
	# return HttpResponse('Hello')


def geninfo(request):
	# return render(request, 'def index(request):
	return render(request, 'mainsite/geninfo.html')
	# return HttpResponse('Hello')')
	# return HttpResponse('Hello')





def sctu(request):
	return render(request, 'mainsite/sctu.html')
	
def infra(request):
	return render(request, 'mainsite/infra.html')

def prmsg(request):
	return render(request, 'mainsite/prmsg.html')



def procedure(request):
	return render(request, 'mainsite/procedure.html')

def age(request):
	return render(request, 'mainsite/age.html')

def academic(request):
	return render(request, 'mainsite/academic.html')

def others(request):
	return render(request, 'mainsite/others.html')
	
def lib(request):
	return render(request, 'mainsite/lib.html')
	
def scilab(request):
	return render(request, 'mainsite/scilab.html')
	
def complab(request):
	return render(request, 'mainsite/complab.html')
	
def hostel(request):
	return render(request, 'mainsite/hostel.html')
	

def signin(request):
	if request.method == 'POST':
		#print('request is post')
		username = request.POST['username']
		password = request.POST['password']
		#print(username)
		#print(password)
		user = authenticate(request, username=username, password=password)
		if user is not None :
			#print('user is not None')
			login(request, user)
			return redirect('personalInfo')
		else :
			param = {'error_message': 'Invalid Credentials'}
			return render(request, 'mainsite/index.html', param)
	
	else :
		#print('method is get')
		return render(request, 'mainsite/index.html')

def signout(request):
	logout(request)
	return redirect('mainsite')

def personalInfo(request):
	return render(request, 'mainsite/personalInfo.html')
def homework(request):
	hw = Homework.objects.filter(standard=request.user.student.standard, divison=request.user.student.divison)
	param = {'homework' : hw}
	return render(request, 'mainsite/homework.html', param)
def reportlaptop(request):
	# result = request.user.student.result_set.all()
	# students = Student.objects.filter(year=)
	if request.method == 'GET':
		return render(request, 'mainsite/report.html', {'hide': 'display: None;', 'class': 10, 'term': 1})
	else :
		result1 = []
		class1 = int(request.POST['class'])
		term = int(request.POST['term'])
		error_message = 'No Records Found'
		final = request.user.student.result_set.filter(standard=class1, term=term)
		
		if len(final) == 0: 
			return render(request, 'mainsite/report.html', {'error_message': error_message, 'hide': 'display: none;', 'class': class1, 'term': term})
		else : 
			students = Student.objects.filter(standard=request.user.student.standard)
			results = Result.objects.filter(student__in=students, exam=final[len(final) - 1].exam, standard=class1)
			school_topper = results.aggregate(Max('Total_obtained_marks'))['Total_obtained_marks__max']
			students = Student.objects.filter(standard=request.user.student.standard, divison=request.user.student.divison)
			results = Result.objects.filter(student__in=students, exam=final[len(final) - 1].exam, standard=class1)
			your_marks = final[len(final) - 1].Total_obtained_marks			
			class_topper = results.aggregate(Max('Total_obtained_marks'))['Total_obtained_marks__max']
			return render(request, 'mainsite/report.html', {'result': final, 'school_topper' : school_topper, 'class_topper': class_topper, 'your_marks': your_marks, 'class': class1, 'term': term})



def subjectAnalysis(request):
	subject = request.GET.get('subject', None)
	standard = request.GET.get('standard', None)
	term1 = request.GET.get('term', None)





	class1 = int(standard)
	term = int(term1)
	# print(class1)
	# print(term1)
	error_message = 'No Records Found'
	final = request.user.student.result_set.filter(standard=class1, term=term)

	if len(final) == 0: 
		JsonResponse({'error': 'No data found'})
	else : 
		students = Student.objects.filter(standard=request.user.student.standard)
		results = Result.objects.filter(student__in=students, exam=final[len(final) - 1].exam, standard= class1)
		school_topper = results.aggregate(Max(subject))[subject + '__max']
		students = Student.objects.filter(standard=request.user.student.standard, divison=request.user.student.divison)
		results = Result.objects.filter(student__in=students, exam=final[len(final) - 1].exam, standard=class1)
		your_marks = request.user.student.result_set.get(term=term, standard=class1, exam=final[len(final) - 1].exam)
		your_marks = getattr(your_marks, subject)
		print(your_marks)
		class_topper = results.aggregate(Max(subject))[subject + '__max']
		# return render(request, 'mainsite/report.html', {'result': final, 'school_topper' : school_topper, 'class_topper': class_topper, 'your_marks': your_marks, 'class': class1, 'term': term})
		data = {
			'school_topper' : school_topper, 'class_topper': class_topper, 'your_marks': your_marks
		}
		return JsonResponse(data)
			
def reportmobile(request):
	if request.method == 'GET':
		return render(request, 'mainsite/academicreportmobile.html', {'hide': 'display: None;', 'class': 10, 'term': 1})
	else :
		result1 = []
		class1 = int(request.POST['class'])
		term = int(request.POST['term'])
		error_message = 'No Records Found'
		final = request.user.student.result_set.filter(standard=class1, term=term)
		
		if len(final) == 0: 
			return render(request, 'mainsite/academicreportmobile.html', {'error_message': error_message, 'hide': 'display: none;', 'class': class1, 'term': term})
		else : 
			print('hre')
			students = Student.objects.filter(standard=request.user.student.standard)
			results = Result.objects.filter(student__in=students, exam=final[len(final) - 1].exam,  standard=class1)
			school_topper = results.aggregate(Max('Total_obtained_marks'))['Total_obtained_marks__max']
			students = Student.objects.filter(standard=request.user.student.standard, divison=request.user.student.divison)
			results = Result.objects.filter(student__in=students, exam=final[len(final) - 1].exam)
			your_marks = final[len(final) - 1].Total_obtained_marks			
			class_topper = results.aggregate(Max('Total_obtained_marks'))['Total_obtained_marks__max']
			return render(request, 'mainsite/academicreportmobile.html', {'result': final, 'school_topper' : school_topper, 'class_topper': class_topper, 'your_marks': your_marks, 'class': class1, 'term': term})


def videolecture(request):
	return render(request, 'mainsite/videolec.html')
def feedback(request):
	return render(request, 'mainsite/feedback.html')
	
def update(request):
	
	# if request.method == 'POST':
    #     name = request.POST['name']
    #     mis = request.POST['mis']
    #     std = request.POST['std']
    #     divison = request.POST['divison']
    #     doa = request.POST['doa']
    #     fatherName = request.POST['fatherName']
    #     fatherOccupation = request.POST['fatherOccupation']
    #     motherName = request.POST['motherName']
    #     motherOccupation = request.POST['motherOccupation']
    #     parentContact1 = request.POST['parentContact1']
    #     parentContact2 = request.POST['parentContact2']
    #     temporaryAddress = request.POST['temporaryAddress']
    #     parmenantAddress = request.POST['parmenantAddress']
    #     studentContact = request.POST['studentContact']
    # else:
		return render(request, 'mainsite/update.html')

def results(request):
	# return render(request, 'mainsite/results.html')
	
	return render(request, 'results.html')


