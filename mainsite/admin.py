from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Notice, School, Year, Student, Result, Tenth_Result, Homework, Tenth_Topper, Profile, District_state, City_district, Address, Subject, Result, Teacher, Teaches
from django.contrib.auth.models import User

# Register your models here.
# Register your models here.


admin.site.register(School)
# admin.site.register(Student)
# admin.site.register(Result)

# admin.site.register(Subject)
admin.site.register(Notice)
# admin.site.register(Standard)
# admin.site.register(Divison)
admin.site.register(Year)
# admin.site.register(Student, StudentAdmin)
admin.site.register(Address)
admin.site.register(District_state)
admin.site.register(City_district)
admin.site.register(Subject)
admin.site.register(Result)
admin.site.register(Teacher)
admin.site.register(Teaches)


class ResultInline(admin.StackedInline):
    model = Result
    can_delete = False
    verbose_name_plural = 'Results'
    extra = 0

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'



class StudentAdmin(admin.ModelAdmin):
	ordering = ('studentname',)
	list_display = ('studentname', 'standard', 'divison', )
	search_fields = ('studentname', 'standard', 'divison', )
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	inlines = (ProfileInline, ResultInline,)
admin.site.register(Student, StudentAdmin)





# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Students'
    


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,)

    

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(Student, StudentAdmin)








class Tenth_TopperInline(admin.StackedInline):
    model = Tenth_Topper
    can_delete = False
    verbose_name_plural = 'Tenth_Toppers'
class Tenth_ResultAdmin(admin.ModelAdmin):
	ordering = ('year',)
	list_display = ('year', 'heading',)
	search_fields = ('year',)
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	exclude = ()
	inlines = (Tenth_TopperInline,)
	extra = 0
	can_delete = True
admin.site.register(Tenth_Result, Tenth_ResultAdmin)
# admin.site.register(Tenth_Result)
# admin.site.register(Tenth_Topper)




admin.site.register(Homework)