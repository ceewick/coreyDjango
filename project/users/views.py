from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

def register(request):
    #  Form to be passed to template
    # can create python classes that create HTML for us. UserCreationForm()
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        ## Is form valid? If True, grab username submitted. 
        if form.is_valid():

            # Save form POST
            form.save()

            # form.cleaned_date = dictionary data from form
            username = form.cleaned_data.get('username')
            
            # Flash 
            # Using F-String - only python 3.6+. Formatted strings
            # messages.success(request, f'Account Created for {username}!')
            
            messages.success(request, f'Your account has been created! You are now able to login')            
            # Redirect user to login
            return redirect('login')
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
    
