from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here. 
def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def signin(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/dashboard/')
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/index/')

def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/signin/')
    
    return render(request, 'signup.html', {'form': form})

def add_student(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = AddStudentForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/signin/')
    
    return render(request, 'signup.html', {'form': form})
