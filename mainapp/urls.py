from django.urls import path
from .import views
from .views import HomePageView,AboutPageView,ContactUsPageView,RoomPageView,BlogPageView,BlogDetailPageView, UpcomingEventDetailPageView

urlpatterns=[
path("", HomePageView.as_view(), name="home"),
path("about-us/", AboutPageView.as_view(), name="about-us"),
path("contact-us/", ContactUsPageView.as_view(), name="contact-us"),
path("rooms/", RoomPageView.as_view(), name="rooms"),
path("blogs/", BlogPageView.as_view(), name="blogs"),
path("blog/<slug>/", BlogDetailPageView.as_view(), name="blog"),
path("upcomingevent/<str:pk>/", UpcomingEventDetailPageView.as_view(), name="upcomingevent"),
path("contactmail/", views.SendContactMail, name="contactmail"),
path("bookroom/", views.SendBookedRoom2Mail, name="bookroom"),
path("newsletter/", views.newsletter, name="newsletter"),
]