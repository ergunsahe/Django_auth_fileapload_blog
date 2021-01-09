from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):
    form = RegistrationForm(request.POST or None)
    if request.user.is_authenticated:
        messages.warning(request, "Youre alreadys registered")
        return redirect("blog:list")
    if form.is_valid():
        form.save()
        name= form.cleaned_data["username"]
        messages.success(request, "You are successfully registered!")
        return redirect("login")
        
    context = {
         "form":form   
    }
    
    return render(request, "users/register.html", context)

def profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        return redirect(request.path)
    
    context = {
        "u_form":u_form,
        "p_form":p_form
    }
    
    return render(request, "users/profile.html", context)
