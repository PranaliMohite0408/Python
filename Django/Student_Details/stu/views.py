import email
from multiprocessing import context
from operator import methodcaller
from django.shortcuts import render,redirect
from stu.models import Student

# Create your views here.

def INDEX(request):
    stu = Student.objects.all()

    context = {
        'stu':stu,
    }
    return render(request, 'index.html',context)

def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mob_no = request.POST.get('mob_no')
        email = request.POST.get('email')
        address = request.POST.get('address')

        stu = Student(
            name = name,
            mob_no = mob_no,
            email = email,
            address = address
        )
        stu.save()
        return redirect('home')


    return render(request, 'index.html')

def edit(request,id):  
    stu = Student.objects.get(id=id)
    context = {
         'stu':stu,
     }
    return render(request,'update.html',context)  

def update(request, id): 
    if request.method == 'POST':
        name = request.POST.get('name')
        mob_no = request.POST.get('mob_no')
        email   = request.POST.get('email')
        address = request.POST.get('address')

        stu = Student(
            id=id,
            name= name,
            mob_no = mob_no,
            email = email,
            address = address
        )
        stu.save()
        return redirect('home')  

    return render(request, 'update.html', {'stu': stu})  

def delete(request , id):
    stu = Student.objects.get(id=id)
    stu.delete()        
    return redirect('home')