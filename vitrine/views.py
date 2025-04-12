from django.shortcuts import redirect, render
from .forms import ContactForm, RequestQuoteForm
from django.views.generic import TemplateView

class RobotsTxtView(TemplateView):
  template_name = "robots.txt"


def index(request):
  if request.method == "POST":
    form1 = ContactForm(request.POST)
    form2 = RequestQuoteForm(request.POST)
    if form1.is_valid or form2.is_valid:
      form1.save()
      form2.save()
      return redirect('site:home')
  
  else:
    form1 = ContactForm()
    form2 = RequestQuoteForm()
    
    context = {
      'form1': form1,
      'form2': form2
    }
  return render(request, "index.html", context)



def page404(request, exception):
    return render(request, "404.html")