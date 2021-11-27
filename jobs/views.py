from django.shortcuts import redirect, render
from jobs.models import Recruiter, StudentUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# Create your views here.


def index(request):
    return render(request, 'index.html')



def admin_login(request):
    error = ''
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error='no'
            else:
                error='yes'
        except:
            error='yes'
    context = {'error':error}
    return render(request, 'admin_login.html',context)


def user_login(request):
    error = ''
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request,user)
                    error='no'
                else:
                    error='yes'
            except:
                error='yes'
        else:
            error='yes'
    context = {'error':error}
    return render(request, 'user_login.html',context)


def recruiter_signup(request):
    error = ''
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['Image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        company = request.POST['company']
        try:
            user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Recruiter.objects.create(user=user,mobile=con,image=i,company=company,gender=gen,type='recruiter',status='pending')
            error = "no"
        except:
            error = "yes"
    context = {'error':error}
    return render(request, 'recruiter_signup.html',context)


def recruiter_login(request):
    error = ''
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status!='pending':
                    login(request,user)
                    error='no'
                else:
                    error='not'
            except:
                error='yes'
        else:
            error='yes'
    context = {'error':error}
    return render(request, 'recruiter_login.html',context)




def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user_home.html')


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    return render(request, 'recruiter_home.html')



def Logout(request):
    logout(request)
    return redirect('index')




def user_signup(request):
    error = ''
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['Image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            StudentUser.objects.create(user=user,mobile=con,image=i,gender=gen,type='student')
            error = "no"
        except:
            error = "yes"
    context = {'error':error}
    return render(request, 'user_signup.html',context)



def view_users(request):
    if not request.user.is_authenticated:
        return redirect('view_users')
    data = StudentUser.objects.all()
    context = {'data':data}
    return render(request, 'view_users.html',context)


def delete_user(request,pk):
    if not request.user.is_authenticated:
        return redirect('view_users')
    student = StudentUser.objects.get(pk=pk)
    student.delete()
    return redirect('view_users')


def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='pending')
    context = {'data':data}
    return render(request, 'recruiter_panding.html',context)