from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login(request): 
    return redirect('home')
    
