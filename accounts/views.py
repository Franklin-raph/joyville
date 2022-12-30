from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser as User




# def loginView(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	page='sign_in'
# 	if  request.method == "POST":
# 		email=request.POST.get('email')
# 		password=request.POST.get('password')
# 		redirect_to=request.POST.get('next')
# 		print(redirect_to,'.........')

# 		try:
# 			user = User.objects.get(email=email)
# 		except:
# 			# messages.error(request, 'User does not exits')
# 			bk=""
# 		user= authenticate(request, email=email, password=password)
# 		if user is not None:
# 			login(request, user)
# 			try:
# 				return redirect(redirect_to)
# 			except:
# 				return redirect('profile', request.user)
# 		else:
# 			messages.error(request, 'User does not exits or invalid credentials')
# 	return render(request, 'accounts/register_login.html', {'page':page} )	

# def registrationView(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	page='reg'
# 	if request.method == "POST":
# 		form=CustomUserCreationForm(request.POST)
# 		# valuenext= request.POST.get('next')
# 		if form.is_valid():
# 			user=form.save(commit =False)
# 			user.is_active = False
# 			user.save()
# 			# login(request,user)
# 			# return redirect('home')

# 			try:
# 				# to get the domain of the current site 
# 				from_email='nwaforglory6@gmail.com'
# 				current_site = get_current_site(request) 
# 				mail_subject = 'Activation link has been sent to your email id'

# 				message = render_to_string('accounts/acc_active_email.html', {  
# 	                'user': user,  
# 	                'domain': current_site.domain,  
# 	                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
# 	                'token':account_activation_token.make_token(user),  
# 	            })

# 				to_email = form.cleaned_data.get('email')
# 				msg = EmailMultiAlternatives(mail_subject, message, from_email, [to_email]) 
# 				msg.attach_alternative(message, "text/html") 
# 				msg.send()  
# 				return render(request, 'accounts/reg_email_set_confirm.html')
# 			except:
# 				User.objects.all().first().delete()
# 	else:
# 		form=CustomUserCreationForm()	
# 	return render(request, 'accounts/register_login.html',{'form':form, 'page':page})



# def logoutView_1(request):
# 	return render(request, 'accounts/register_login.html')

# def logoutView(request):
# 	logout(request)
# 	return redirect('home')




