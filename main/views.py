from django.shortcuts import render, redirect
from .models import Attendance
# Create your views here.

def attendance_view(request):
    status = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            if Attendance.objects.filter(student=request.user).count() > 0:
                status = 1
            else:
                status = 2

            if status == 2:
                attendance = Attendance(student=request.user)
                attendance.save()
        else:
            return redirect('/login/')
    return render(request, "main/attendance.html", {'status': status})

def homepage(request):
    if request.user.is_authenticated:
        return redirect('/attendance/')

    return redirect('/register/')