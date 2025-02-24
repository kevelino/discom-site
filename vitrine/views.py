from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.views.generic import TemplateView

class RobotsTxtView(TemplateView):
  template_name = "robots.txt"


def index(request):
  form = ContactForm()
  
  context = {
    'form': form
  }
  
  return render(request, "index.html", context)



def page404(request, exception):
    return render(request, "404.html")