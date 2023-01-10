from django.shortcuts import render
from django.http import HttpResponse,  JsonResponse
from django.views.generic import TemplateView, ListView,DetailView
from .models import Blog, Newsletter, UpcomingEvent
from django.core.mail import send_mail, BadHeaderError
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class HomePageView(TemplateView):
	template_name="mainapp/index.html"

	def get_context_data(self, *args, **kwargs):
		context=super().get_context_data(**kwargs)
		context["blogs"]=Blog.objects.all()[:10]
		context['upcomingevents']=UpcomingEvent.objects.filter(eventpast=False)
		return context

class AboutPageView(TemplateView):
	template_name="mainapp/about.html"

class ContactUsPageView(TemplateView):
	template_name="mainapp/contact.html"

class RoomPageView(TemplateView):
	template_name="mainapp/rooms.html"

	def get_context_data(self, *args, **kwargs):
		context=super().get_context_data(**kwargs)
		context['rooms']="rooms"
		return context

class BlogPageView(ListView):
	model=Blog
	template_name="mainapp/blog.html"
	context_object_name="blogs"

	def get_context_data(self, *args, **kwargs):
		context=super().get_context_data(**kwargs)
		context["latesblogs"]=Blog.objects.all()[:5]
		return context

class BlogDetailPageView(DetailView):
	template_name="mainapp/blog-details.html"
	context_object_name="blog"
	model=Blog

	def get_context_data(self, *args, **kwargs):
		context=super().get_context_data(**kwargs)
		context["blogs"]=Blog.objects.all()[:7]
		return context

@csrf_exempt
def SendContactMail(request):
	if request.method =="POST" or request.is_ajax:

		name=request.POST["name"]
		from_email=request.POST["email"]
		subject=request.POST["subject"]
		phone=request.POST["phone"]
		message=request.POST["message"]


	try:
			send_mail(subject, message, from_email, ["nwaforglory6@gmail.com"])
	except BadHeaderError:
		return HttpResponse('invalid header found.')

	return HttpResponse('Sent !! Thank you.')

@csrf_exempt
def SendBookedRoom2Mail(request):
	if request.method =="POST" or request.is_ajax:

		firstname=request.POST["firstname"]
		print(firstname,"firstname")
		lastname=request.POST["lastname"]
		print(lastname,"lastname")
		arrival=request.POST["arrival"]
		print(arrival,"arrival")
		depature=request.POST["depature"]
		email=request.POST["email"]
		PhoneNumber=request.POST["PhoneNumber"]
		adults=request.POST["adults"]
		childern=request.POST["childern"]
		roomPrefrence=request.POST["roomPrefrence"]
		subject="New Room Booking Request"

		message=f'''
		Dear Joyvile Hotel, 

		{firstname} {lastname} has just booked a room. Details below:

		Name : {firstname} {lastname},
		Email: {email},
		Arrival: {arrival},
		Departure: {depature},
		PhoneNumber: {PhoneNumber},
		No of Adults :{adults},
		No of Children: {childern},
		Preferred Room: {roomPrefrence},

		'''




	try:
			send_mail(subject, message, email, ["nwaforglory6@gmail.com"])
	except BadHeaderError:
		return HttpResponse('invalid header found.')

	return JsonResponse({"msg": "Room Booked successfully, we'll get back to you within the next 24 hours via your mail. !! Thank you."})
	
@csrf_exempt
def newsletter(request):
	if request.method =="POST":
		Newsletter.objects.create(email=request.POST["email"])
	return HttpResponse('Subscribed !! Thank you.')



def handler404(request, exception):
	return render(request, 'mainapp/404.html', status=404)


