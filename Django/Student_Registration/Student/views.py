from django.shortcuts import render, redirect
from Student.models import User
# Create your views here.

def Index(request):
    stu = User.objects.all()
    
    context = {
        'stu':stu,
    }

    return render(request, 'index.html',context)

def ADD(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mob_no = request.POST.get('mob_no')
        email = request.POST.get('email')
        address = request.POST.get('address')

        stu = User(
            name = name,
            mob_no = mob_no,
            email = email,
            address = address
        )
        stu.save()
        return redirect('home')

        return render(request, 'index.html')

def Edit(request):
    stu = User.objects.all()
    
    student = {
        'stu':stu,
    }

    return render(request, 'index.html',student)

    