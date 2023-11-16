from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
	tasks=Task.objects.all()
	form=TaskForm()
	points=Total.objects.get(id=1)	
	if request.method=='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			points.allPoints=points.allPoints+int(request.POST.get("points"))
			points.save()
			form.save()
		return redirect('/')
	context={'form':form,'tasks':tasks,'points':points}
	return render(request,"tasks/list.html", context)
def updateTask(request, pk):
	task=Task.objects.get(id=pk)
	currPoints=task.points
	complete=task.complete
	form=TaskForm(instance=task)
	points=Total.objects.get(id=1)	
	if request.method=='POST':
		form=TaskForm(request.POST,instance=task)
		if form.is_valid():
			points.allPoints=points.allPoints-currPoints+int(request.POST.get("points"))
			print(request.POST.get("complete"))
			if complete==False and request.POST.get("complete")=="on":
				points.finished=points.finished+int(request.POST.get("points"))
			if complete==True and request.POST.get("complete")!="on":
				points.finished=points.finished-int(request.POST.get("points"))
			if complete==True and request.POST.get("complete")=="on":
				points.finished=points.finished-currPoints+int(request.POST.get("points"))
			points.save()	
			form.save()  
			return redirect('/')
	context={'form':form}
	return render(request,'tasks/update_task.html', context)  
def deleteTask(request, pk):
	task=Task.objects.get(id=pk)
	points=Total.objects.get(id=1)
	if request.method=='POST':
		points.allPoints=points.allPoints-task.points
		if task.complete==True:
			points.finished=points.finished-task.points
		points.save()	
		task.delete()
		return redirect('/')
	context={'task':task}
	return render(request,'tasks/delete_task.html',context)
def completedTask(request):
	task=Task.objects.filter(complete=True)
	form=TaskForm()
	points=Total.objects.get(id=1)	
	if request.method=='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			points.allPoints=points.allPoints+int(request.POST.get("points"))
			points.save()
			form.save()
		return redirect('/')
	context={'tasks':task,'form':form,'points':points}
	return render(request,'tasks/list.html',context)

def uncompletedTask(request):
	task=Task.objects.filter(complete=False)
	form=TaskForm()
	points=Total.objects.get(id=1)
	if request.method=='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			points.allPoints=points.allPoints+int(request.POST.get("points"))
			points.save()
			form.save()
		return redirect('/')
	context={'tasks':task,'form':form,'points':points}
	return render(request,'tasks/list.html',context)		