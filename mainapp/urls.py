from django.urls import path
from .import views
from .views import HomePageView,AboutPageView,ContactUsPageView,RoomPageView,BlogPageView

urlpatterns=[
path("", HomePageView.as_view(), name="home"),
path("about-us/", AboutPageView.as_view(), name="about-us"),
path("contact-us/", ContactUsPageView.as_view(), name="contact-us"),
path("rooms/", RoomPageView.as_view(), name="rooms"),
path("blogs/", BlogPageView.as_view(), name="blogs"),
]