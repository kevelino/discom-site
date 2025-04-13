from django.urls import path
from . import views


app_name = "site"

urlpatterns = [
  path("", views.index, name="home"),
  path("request-a-quote", views.requestQuote, name="request_quote"),
  path("contact-us", views.contactUs, name="contact_us"),
]
