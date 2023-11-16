from django.db import models

# Create your models here.
class Task(models.Model):
	title=models.CharField(max_length=200)
	complete=models.BooleanField(default=False)
	created=models.DateTimeField(auto_now_add=True)
	points=models.IntegerField(default=0)

	def __str__(self):
		return self.title
"""	def update(self,add):
		self.title=self.title+add
		self.save()
	def setpoints(self):
		if points>10:
			self.points=100
		self.save()
	def setcomplete(self):
		if complete==False:
			self.complete=True
		elif complete==True:
			self.complete=False
		self.save()
class Student(models.Models):
	name=models.CharField(max_length=200)
	number=models.IntegerField()
	section=models.CharField(max_length=5)
    grade=models.FloatField()
    age=models.IntegerField()
    def upgradegrade(self,newgrade):
    	self.grade=(self.grade+newgrade)/2
    	self.save()"""
class Total(models.Model):
	finished=models.IntegerField(default=0)
	allPoints=models.IntegerField(default=0)



