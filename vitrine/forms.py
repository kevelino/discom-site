from django import forms
from django.utils.translation import gettext_lazy as _
from django_recaptcha.fields import ReCaptchaField



class ContactForm(forms.Form):
    
    full_name = forms.CharField(
        max_length=100, 
        label=_("Nom complet"),
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control bg-light border-0', 'placeholder': _('Votre nom')})
    )
    
    subject = forms.CharField(
        label = _("Sujet de votre message"),
        required=True,
        widget=forms.TextInput(attrs={
                'class':'form-control bg-light border-0',
                'placeholder':_("L'objet de votre message")
    }))
    
    email = forms.EmailField(
        label=_("Adresse e-mail"),
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control bg-light border-0', 'placeholder': _('Votre email')})
    )
    
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control bg-light border-0', 'rows': 3, 'placeholder': _('Message')})
    )
    
    captcha = ReCaptchaField(
        label='',
        required=True,
        error_messages={
            'required': _('Veuillez compléter le reCAPTCHA pour soumettre le formulaire.')},
        )
            

class RequestQuoteForm(forms.Form):
    """Formulaire de demande de devis personnalisé."""

    nom = forms.CharField(
        max_length=100,
        label="Nom complet",
        widget=forms.TextInput(attrs={'class': 'form-control bg-light border-0', 'placeholder': _('Votre nom')})
    )

    email = forms.EmailField(
        label="Adresse email",
        widget=forms.EmailInput(attrs={'class': 'form-control bg-light border-0', 'placeholder': 'email@exemple.com'})
    )

    entreprise = forms.CharField(
        required=False,
        max_length=100,
        label="Nom de l'entreprise",
        widget=forms.TextInput(attrs={'class': 'form-control bg-light border-0', 'placeholder': _('Nom de l’entreprise')})
    )

    service = forms.ChoiceField(
        choices=[
            ('', _('----------Sélectionner un service----------')),
            ('site_web', 'Création de site web'),
            ('marketing', 'Services digitaux'),
            ('securite', 'Système de vidéosurveillance'),
            ('energie', "Contrôle d'accès"),
            ('energie', 'Portails automatiques'),
            ('energie', 'Réseaux Informatiques'),
            ('energie', 'Électricité bâtiment'),
            ('energie', 'Énergie solaire photovoltaïque'),
        ],
        label="Service souhaité",
        widget=forms.Select(attrs={'class': 'form-control bg-light border-0'})
    )

    message = forms.CharField(
        label="Détails de la demande",
        widget=forms.Textarea(attrs={'class': 'form-control bg-light border-0', 'rows': 3, 'placeholder': _('Expliquez votre besoin...')})
    )

    
    captcha = ReCaptchaField(
        label='',
        required=True,
        error_messages={
            'required': _('Veuillez compléter le reCAPTCHA pour soumettre le formulaire.')
        })
    
