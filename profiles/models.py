from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Interest(models.Model):
	name = models.CharField(max_length=50, default='Medical Health')
	def __str__(self):
		return str(self.name)

class Badge(models.Model):
	name = models.CharField(max_length=50, default='none')
	def __str__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=50, default='none')
	interest = models.ForeignKey(Interest, default=1)
	content = models.CharField(max_length=50, blank=True)
	class Meta:
		permissions = (
			("can_create_team_profile", "Can create team profile"),
			("can_edit_team_profile", "Can edit team profile"),

		)
	def __str__(self):
		return self.name
class Role(models.Model):
	name = models.CharField(max_length=50, default='none')
	def __str__(self):
		return self.name


class Student(models.Model):
	#name = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.ForeignKey(User, unique=True,)
	realname = models.CharField(max_length=50, default='')
	nickname = models.CharField(max_length=50)
	department = models.CharField(max_length=50)
	motto = models.CharField(max_length=20, blank=True)
	interest = models.ForeignKey(Interest, default=1)
	talent = models.CharField(max_length=20, blank=True)
	#talent = models.ManyToManyField(Talent, default=1 )#one student can have many badges, one badge can have many students
	badge = models.ManyToManyField(Badge, default=1 )#one student can have many badges, one badge can have many students
	role = models.ForeignKey(Role, default=1)
	team = models.ForeignKey(Team, default=1 )
	follow = models.ManyToManyField('self', blank=True, symmetrical=False)
	applied = models.ManyToManyField(Team, blank=True, related_name='applier')
	class Meta:
		permissions = (
			("can_edit_base_profile", "Can edit base profile"),
			("can_view_base_profile", "Can view base profile"),

		)
	def __str__(self):
		return self.realname

class Chatroom(models.Model):
	student1 = models.ForeignKey(Student, null=True, related_name='student1')
	student2 = models.ForeignKey(Student, null=True, related_name='student2')
	content = models.CharField(max_length=50)
	date_time = models.DateTimeField()
	def __str__(self):
		return self.content

class up_file(models.Model):
	upload_datetime = models.DateTimeField()
	student = models.ForeignKey(Student, null=True)
	def __str__(self):
		return self.student.realname

class file_info(models.Model):
	File = models.ForeignKey(up_file, null=True)
	local_name = models.CharField(max_length=50)
	upload_name = models.CharField(max_length=50)
	def __str__(self):
		return self.upload_name

class Teamroom(models.Model):
	team = models.ForeignKey(Team, null=True)
	speaker = models.ForeignKey(Student, null=True)
	content = models.CharField(max_length=50)
	date_time = models.DateTimeField()
	def __str__(self):
		return self.content

