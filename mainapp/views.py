from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView,DetailView
from .models import Blog, Newsletter, UpcomingEvent
from django.core.mail import send_mail, BadHeaderError
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

def newsletter(request):
	if request.method =="POST":
		Newsletter.objects.create(email=request.POST["email"])
	return HttpResponse('Subscribed !! Thank you.')






