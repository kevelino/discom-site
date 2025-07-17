from django.shortcuts import redirect, render
from django.http import JsonResponse
from .forms import ContactForm, RequestQuoteForm
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail

class RobotsTxtView(TemplateView):
  template_name = "robots.txt"

def send_quote_email(request, forms):
    current_site = get_current_site(request)
    subject = "Demande de devis"
    
    message = render_to_string("emails/send_quote.txt", {
        'current_site': current_site,
        'full_name': forms[0],
        'email': forms[1],
        'company': forms[2],
        'service': forms[3],
        'message': forms[4],
    }) 
    
    try:
        send_mail(
            subject=subject, 
            message=message, 
            from_email=settings.EMAIL_HOST_USER, 
            recipient_list=[forms[1]])
    except Exception:
        return False

def index(request):
  contact_form = ContactForm()
  request_quote_form = RequestQuoteForm()
  
  context = {
    'contact_form': contact_form,
    'request_quote_form': request_quote_form
  }
  return render(request, "index.html", context)


def requestQuote(request):
  request_quote_form = RequestQuoteForm()
  if request.method == "POST":
    request_quote_form = RequestQuoteForm(request.POST)
    if request_quote_form.is_valid():
      name = request_quote_form.cleaned_data.get('nom')
      email = request_quote_form.cleaned_data.get('email')
      company = request_quote_form.cleaned_data.get('entreprise')
      service = request_quote_form.cleaned_data.get('service')
      message = request_quote_form.cleaned_data.get('message')
      
      forms = [name, email, company, service, message]
      # Send an email
      send_quote_email(request, forms)
      return JsonResponse({'success': True})
    else:
      print(request_quote_form.errors)
      return JsonResponse({'success': False, 'errors': request_quote_form.errors.as_ul()})
  return JsonResponse({'success': False, 'errors': 'Requête invalide.'}) 


def contactUs(request):
  contact_form = ContactForm()
  if request.method == "POST":
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
      full_name = contact_form.cleaned_data.get('full_name')
      email = contact_form.cleaned_data.get('email')
      subject = contact_form.cleaned_data.get('subject')
      message = contact_form.cleaned_data.get('message')
      
      # Send an email
      send_mail(
        subject, #Sujet du message
        f'Message de {full_name} <{email}> \n\n',
        message, # Message
        None,  # From email
        [settings.ADMIN_EMAIL],  # To email
        # fail_silently=False,
      )
      
      return JsonResponse({'success': True})
    else:
      print(contact_form.errors)
      return JsonResponse({'success': False, 'errors': contact_form.errors.as_ul()})
  return JsonResponse({'success': False, 'errors': 'Requête invalide.'}) 
    


def page404(request, exception):
    return render(request, "404.html")