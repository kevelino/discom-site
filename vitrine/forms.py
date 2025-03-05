from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _
from django_recaptcha.fields import ReCaptchaField



class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(
        label='',
        required=True,
        error_messages={
            'required': 'Veuillez compléter le reCAPTCHA pour soumettre le formulaire.'
        })
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'subject', 'message')
        widgets = {
            'full_name':forms.TextInput(attrs={
                'class':'form-control bg-light border-0',
                'placeholder':_('Votre Nom')
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control bg-light border-0',
                'placeholder':_('Votre Email')
            }),
            'subject':forms.TextInput(attrs={
                'class':'form-control bg-light border-0',
                'placeholder':_("L'objet de votre message")
            }),
            'message':forms.Textarea(attrs={
                'class':'form-control bg-light border-0',
                'rows':3,
                'placeholder':_('Message')
            }),
        }


