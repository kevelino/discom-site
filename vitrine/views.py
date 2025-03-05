from django.shortcuts import redirect, render
from .models import Contact
from .forms import ContactForm
from django.views.generic import TemplateView

class RobotsTxtView(TemplateView):
  template_name = "robots.txt"


def index(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('site:home')
  
  else:
    form = ContactForm()
    
    context = {
      'form': form
    }
  return render(request, "index.html", context)



def page404(request, exception):
    return render(request, "404.html")