from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Image
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all().order_by('-post_date')
    users = User.objects.all()  
    current = request.user
    
    return render(request, 'index.html',{"images":images,'users':users,'current':current,})