from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee ,Employee_leaves
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
EMAIL_HOST_USER = 'adithyanajith92@gmail.com'
import plotly.graph_objects as go
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(password,"password",username,"username")
        employee = authenticate(username=username, password=password)
        if employee is not None:
            login(request, employee)
            return redirect('/')
        else:
            messages.info(request, "invalid login")
            return redirect('index')
    return render(request,'login.html')


def manage_employee(request):
    data = Employee.objects.all()
    return render(request, 'manageEmployee.html', {'data': data})

@login_required()
def create_employee(request):
    if request.method == 'POST':
        print(request.POST.dict(),"[[[[[[[[[[[[[")
        # employee_id=request.POST['employee_id']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        designation = request.POST['designation']
        team = request.POST['team']
        salary = request.POST['salary']
        phonenumber = request.POST['phone']

        employee = Employee(firstname=firstname, lastname=lastname, email=email,
                            designation=designation, team=team, salary=salary,
                            phonenumber=phonenumber)
        employee.save()
        return redirect('manage_employee')
    return render(request, 'createEmployee.html')

@login_required()
def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.firstname = request.POST['firstname']
        employee.lastname = request.POST['lastname']
        employee.email = request.POST['email']
        employee.designation = request.POST['designation']
        employee.team = request.POST['team']
        employee.salary = request.POST['salary']
        employee.phonenumber = request.POST['phone']
        employee.save()
        return redirect('manage_employee')
    return render(request, 'editEmployee.html',{'a':employee})

@login_required()
def delete_employee(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/manage/")

@login_required()
def employee_leaves(request):
    employee_leaves = Employee_leaves.objects.all()
    context = {
        'employee_leaves': employee_leaves
    }
    return render(request, 'employee_leave_list.html',context)


def CreateLeave(request):
    context = {}
    context['emp_ids'] = request.GET.get('employ_id')

    if request.method == 'POST':
        print(request.POST.dict())
        mail='adithyan@codesvera.com'

        employee = Employee.objects.get(id=context['emp_ids'])
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        leave_type = request.POST.get('leave_type')
        purpose = request.POST.get('purpose')

        employee_leave = Employee_leaves(
            employee=employee,
            from_date=from_date,
            to_date=to_date,
            leave_type=leave_type,
            purpose=purpose
        )
        employee_leave.save()
        send_gmail(mail,employee,from_date,to_date,purpose)

        return redirect('employee_leaves')

    return render(request, 'create_leave.html', context)


def send_gmail(email, employee, from_date, to_date, purpose):
    subject = "Leave Applied"
    message = f'Hi,{employee} is on leave from {from_date} to {to_date} due to {purpose}'
    email_from =EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)


import plotly.graph_objects as go
from django.shortcuts import render
from .models import Employee


def salary_graph(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'graph.html', context)













