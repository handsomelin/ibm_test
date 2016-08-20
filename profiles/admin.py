from django.contrib import admin
from profiles.models import Student, Interest, Talent, Badge, Team, Follow
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

'''
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'
# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (StudentInline, )
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
'''
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'nickname', 'department')
	

admin.site.register(Student, StudentAdmin)
admin.site.register(Interest)
admin.site.register(Talent)
admin.site.register(Badge)
admin.site.register(Team)
admin.site.register(Follow)