from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
def homePageView(request):
    return HttpResponse('Hello, World!')

@login_required(login_url='/accounts/login/')
def instagram(request):
    posts = Image.get_images()
    return render(request, "", {"posts":posts})