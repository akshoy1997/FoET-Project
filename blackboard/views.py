from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

def homeView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'index.html')

def studentView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'student.html')

def teacherView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'teacher.html')

def registerView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})