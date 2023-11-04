from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps,
    }
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role = request.POST.get('role')  # Assuming 'role' is a foreign key
        dept = request.POST.get('dept')  # Assuming 'dept' is a foreign key
        salary=request.POST.get('salary')
        bonus=request.POST.get('bonus')
        phone =request.POST.get('phone')
        hire_date=request.POST.get('hire_date')
        if first_name and last_name and role and dept:
            new_Emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hire_date=hire_date)
            new_Emp.save()
            return HttpResponse('Employee added successfully')
        else:
            return HttpResponse('Invalid input. Please fill in all fields.')

    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_remove=Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse("remove succefully")
        except:
            return HttpResponse('key not found')
    emps=Employee.objects.all()
    contex={
        'emps':emps,
    }

    return render(request, 'remove_emp.html',contex)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)| Q(last_name__icontains= name))
        if dept:
            emps= emps.filter(dept__name =dept)
        if role:
            emps = emps.filter(role__name=role)
        contex={
            'emps':emps,
        }
        return render(request,'all_emp.html')
    elif request.method =='GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('Error hai bhai')
