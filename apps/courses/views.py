from django.shortcuts import render, redirect
from .models import Course
# Create your views here.


def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "courses/index.html", context)

def create(request):
    print "creating course"
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])

    return redirect('/')

def edit(request, id):
    print "editing course"
    context = {
        "course":Course.objects.get(id=id)
    }
    return render(request, 'courses/delete.html', context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
