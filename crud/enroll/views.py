from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User


# Create your views here.
def add_n_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            # fm.save()
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/')
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/add_show.html', {'form': fm, 'stu': stud})


def delete_data(request, my_id):
    if request.method == 'POST':
        pi = User.objects.get(pk=my_id)
        pi.delete()
        return HttpResponseRedirect('/')


def update_data(request, my_id):
    if request.method=='POST':
        pi=User.objects.get(pk=my_id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=my_id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/update_student.html',{'form':fm})
