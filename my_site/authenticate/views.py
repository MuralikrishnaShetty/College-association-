from pickle import TRUE
from tkinter.tix import TEXT
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm,  ProfileForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from datetime import datetime, date
from .models import Post, Finance
import smtplib
# Create your views here.
def home(request): 
	return render(request, 'authenticate/home.html', {})

def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Youre logged in'))
			return redirect('home') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error logging in'))
			return redirect('login') #re routes to login page upon unsucessful login
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('home')

def register_user(request):
	if request.method =='POST':
		form = ProfileForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Youre now registered'))
			return redirect('home')
	else: 
		form = ProfileForm() 
	context = {'form': form}
	return render(request, 'authenticate/register.html', context)

def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have edited your profile'))
			return redirect('home')
	else: 		#passes in user information 
		form = EditProfileForm(instance= request.user) 

	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)
	#return render(request, 'authenticate/edit_profile.html',{})



def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password'))
			return redirect('home')
	else: 		#passes in user information 
		form = PasswordChangeForm(user= request.user) 

	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)

def no_permission(request):
	return render(request, 'authenticate/nopermission.html')

def save_post(request):
	cont = request.POST.get('post_content')
	time = datetime.now().time()
	dates = date.today()
	fname = request.user.first_name
	lname = request.user.last_name
	obj = Post(date= dates, time=time, content=cont, fname=fname, lname=lname)
	obj.save()
	recievers=[]
	for user in User.objects.all():
		recievers.append(user.email)
	sender_add='helpatwork23@gmail.com' 
	password='gkuufogsubzuqpam' 
	smtp_server=smtplib.SMTP("smtp.gmail.com",587)
	smtp_server.ehlo()
	smtp_server.starttls()
	smtp_server.ehlo() 
	smtp_server.login(sender_add,password) 
	messege = "A new Post has been added to SIT website. \nLogin to view \n\n\n\n\nRegards, \nTeam SIT"
	for user in recievers :
		try :
			smtp_server.sendmail(sender_add,user,messege)
		except:
			pass
	smtp_server.quit()
	messages.success(request, ('Your post has been saved successfully'))
	return redirect('home')

@login_required(login_url = '/login')
@user_passes_test(lambda u: u.is_staff, login_url='/nopermission')
def add_post (request):
		return render(request, 'authenticate/add_post.html')

@login_required(login_url = '/login')
def show_post (request):
	posts = Post.objects.all()
	return render(request,'authenticate/showpost.html', {'posts':posts})
	

@login_required(login_url = '/login')
@user_passes_test(lambda u: u.is_staff, login_url='/nopermission')
def add_finance (request):
		return render(request, 'authenticate/add_finance.html')
	
def save_finance(request):
	event  = request.POST.get('event')
	cost = request.POST.get('cost')
	time = datetime.now().time()
	dates = date.today()
	fname = request.user.first_name
	lname = request.user.last_name
	obj = Finance(date= dates, time=time, event=event, cost=cost, fname=fname, lname=lname)
	obj.save()	 
	recievers=[]
	for user in User.objects.all():
		recievers.append(user.email)
	sender_add='helpatwork23@gmail.com' 
	password='gkuufogsubzuqpam' 
	smtp_server=smtplib.SMTP("smtp.gmail.com",587)
	smtp_server.ehlo()
	smtp_server.starttls()
	smtp_server.ehlo() 
	smtp_server.login(sender_add,password) 
	messege = "A new finance detils has been added to SIT website. \nLogin to view \n\n\n\n\nRegards, \nTeam SIT"
	for user in recievers :
		try :
			smtp_server.sendmail(sender_add,user,messege)
		except:
			pass
	smtp_server.quit()
	messages.success(request, ('The Finance  has been saved successfully'))
	return redirect('home')

@login_required(login_url = '/login')
def show_finance (request):
	finances = Finance.objects.all()
	return render(request,'authenticate/showfinance.html', {'finances':finances})