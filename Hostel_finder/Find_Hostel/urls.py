
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="HostelHome"),
    path("hostels/<int:myid>", views.hostels, name="Hostels"),
    path("contact/", views.contact, name="ContactUs"),
    path("about/", views.aboutus, name="AboutUs"),
    path("register", views.register, name="Register"),
    path("search/", views.search, name="search"),
    path("login", views.signin, name="login"),
    path("logout", views.signout, name="logout")
    ]
