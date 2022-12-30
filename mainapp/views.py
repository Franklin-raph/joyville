from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
	template_name="mainapp/index.html"

class AboutPageView(TemplateView):
	template_name="mainapp/about.html"

class ContactUsPageView(TemplateView):
	template_name="mainapp/contact.html"

class RoomPageView(TemplateView):
	template_name="mainapp/rooms.html"

class BlogPageView(TemplateView):
	template_name="mainapp/blog.html"



