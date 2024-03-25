from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
    """The home page for Account."""
    return render(request, 'users_app/registration/login.html')

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to topics page.
            login(request, new_user)
        return redirect('main_homepage_app:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'users_app/registration/register.html', context)
