from django.shortcuts import render,HttpResponse

from home.models import Task

def home(request):
    context={'success':False}
    if request.method=="POST":
        title = request.POST.get('title')
        desc=request.POST.get('desc')
        ins=Task(taskTitle=title,taskDescription=desc)
        ins.save()
        context={'success':True}
    return render(request,'index.html',context)
   
def tasks(request):
    allTasks=Task.objects.all()
    context={'tasks':allTasks}
    for item in allTasks:
        print(item.taskTitle)
    return render(request,'tasks.html',context)
