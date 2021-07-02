from django import forms
from django.shortcuts import render, redirect
from register.forms import RegisterForm
from django.contrib import messages
# Create your views here.


def register(response):
    if response.method == 'POST': 
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        # return redirect("/")
        messages.success(response, 'The form has been successfully submitted!!!') 
        resp = render(response,'register.html',{'form':form})
    else:
        form = RegisterForm()
        resp = render(response,'register.html',{'form':form})
    return resp