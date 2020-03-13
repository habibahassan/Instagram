from django.shortcuts import render,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
from .models import Image,Profile,Like,Followers,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm,PostImage,CommentForm,UpdateImage
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate
from .forms import UserSignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.core.mail import EmailMessage


def usersignup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('activation_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
    else:
        form = UserSignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})
def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all().order_by('-post_date')
    users = User.objects.all()  
    current = request.user
    likes = Like.objects.all().count()
    
    return render(request, 'index.html',{"images":images,'users':users,'current':current,"likes":likes})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user

    if current_user.id == current_user:
        images = Image.objects.all()
        user = request.user
        try:
            profile = Profile.objects.all()
        except ObjectDoesNotExist:
            return redirect(update_profile)
    else:
        images = Image.objects.all()
        user = request.user
        try:
            profile = Profile.objects.all()
        except ObjectDoesNotExist:
            
            return "No profile"     
            
    return render(request,'profile/profile.html',{'user':user,'profile':profile,'images':images,'current_user':current_user})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id=current_user.id
            profile.save()
            return redirect(home)
    else:
        form = UpdateProfileForm()
    return render(request,'profile/update_profile.html',{'user':current_user,'form':form})

def no_profile(request,id):
    
    user = User.objects.get(id=id)
    return render(request,'profile/no_profile.html',{"user":user})

def search_results(request):
    profile = Profile.objects.all
    
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        
        searched_users = User.objects.filter(username__icontains=search_term)
        
        message = f"{search_term}"
        
        return render(request, 'searched.html',{"message":message, "users": searched_users})
        


    else:
        message = "Please input a name in the search form"
        return render(request, 'searched.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
        
    if request.method == 'POST':
        form = PostImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = current_user
            image.profile = current_user.profile            
            image.save()
        return redirect(home)
    else:
        form = PostImage()
        
    return render(request, 'new_image.html', {'user':current_user,"form": form})

@login_required(login_url='/accounts/login/')   
def comment(request,c_id):
    comments = Comment.objects.filter(image_id=c_id)
    current_user = request.user
    current_image = Image.objects.get(id=c_id)
    try:
        likes = Like.objects.filter(post_id=c_id).count()
    except ObjectDoesNotExist:
        likes =0
    try:
        like = Like.objects.filter(post_id=c_id).get(user_id=request.user)
    except ObjectDoesNotExist:
        like =0
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = current_image
            comment.user = current_user   
            comment.save()
            return redirect(home)
    else:
        form = CommentForm()
        
    return render(request,'comments.html',{"form":form,'comments':comments,"image":current_image,"user":current_user,'like':like,"likes":likes})   

def like_pic(request, pic_id):
    current_user = request.user
    
    image = Image.objects.get(id=pic_id)
    new_like = Like(post=image,user=current_user)
    new_like.save()
    return redirect(comment,image.id)

def follow(request,user_id):
    current_user = request.user
    to_follow = Profile.objects.get(user_id=user_id)
    new_profile = Profile(user_id=to_follow,followers=current_user.id,following=to_follow)
    new_profile.save()
    return redirect(home)  

@login_required(login_url='/accounts/login/')
def update_image(request,id):
    current_user = request.user
    image = Image.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateImage(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = current_user
            image.update_image(current,new)
            return redirect(home)
    else:
        form = UpdateImage()

    return render(request,'update_image.html',{'user':current_user,'form':form,"image":image})