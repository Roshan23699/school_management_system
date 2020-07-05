from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	path('', views.index, name = 'mainsite'),
	path('geninfo/', views.geninfo, name = 'geninfo'),
	path('sctu/', views.sctu, name = 'sctu'),
	path('infra/', views.infra, name = 'infra'),
	path('prmsg/', views.prmsg, name = 'prmsg'),
	path('procedure/', views.procedure, name = 'procedure'),
	path('age/', views.age, name = 'age'),
	path('academic/', views.academic, name = 'academic'),
	path('others/', views.others, name = 'others'),
	path('lib/', views.lib, name = 'lib'),
	path('scilab/', views.scilab, name = 'scilab'),
	path('complab/', views.complab, name = 'complab'),
	path('hostel/', views.hostel, name = 'hostel'),
	path('signin/', views.signin, name = 'signin'),
	path('personalInfo/', views.personalInfo, name = 'personalInfo'),
	path('homework/', views.homework, name = 'homework'),
	path('feedback/', views.feedback, name = 'feedback'),
	path('videolecture/', views.videolecture, name = 'videolecture'),
	path('reportlaptop/', views.reportlaptop, name = 'reportlaptop'),
	path('reportmobile/', views.reportmobile, name = 'reportmobile'),
	path('update/', views.update, name = 'update'),
	path('results/', views.results, name='results'),
	path('logout/', views.signout, name='logout'),
    # url(r'^news/$', views.news, name='news'),
    # url(r'^location/$', views.location, name='location'),
    # url(r'^notices/$', views.notices, name='notices'),
	url(r'^ajax/subjectAnalysis/$', views.subjectAnalysis, name='subjectAnalysis'),
	
]