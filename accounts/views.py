from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from accounts.form import SignInForm, SignUpForm
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  
        
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    if request.method == 'GET':
        form = SignInForm()
    elif request.method == 'POST':
        form = SignInForm(request, data=request.POST) # 위에 signup()함수와 다른데요??
        if form.is_valid():
            email = form.cleaned_data.get('username') # cleaned_data??
            password = form.cleaned_data.get('password') # cleaned_data??
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_list')  # Redirect to the 'todo_list' after successful login
            else:
                messages.error(request) # error request
            
    return render(request, 'accounts/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')