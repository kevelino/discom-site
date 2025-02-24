from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


class Contact(models.Model):
  
  """Model definition for Contact."""
  full_name = models.CharField(_("Nom complet"), max_length=200)
  ref = models.CharField(_("Référence"), max_length=50, editable=False, default=uuid4())
  email = models.EmailField(_("Email"), max_length=254)
  message = models.TextField(_("Message"))
  subject = models.CharField(_("Sujet"), max_length=250)
  created_at = models.DateTimeField(_("Créer le"), auto_now_add=True)

  class Meta:
    """Meta definition for Contact."""

    verbose_name = _('Contact')
    verbose_name_plural = _('Contacts')

  def __str__(self):
    """Unicode representation of Contact."""
    return self.full_name
  
  

class Service(models.Model):
  """Model definition for Service."""
  name = models.CharField(_("Nom"), max_length=200)
  description = models.TextField(_("Description"), blank=True, null=True)
  ref = models.CharField(_("Référence"), max_length=50, editable=False, default=uuid4())

  class Meta:
    """Meta definition for Service."""

    verbose_name = _('Service')
    verbose_name_plural = _('Services')

  def __str__(self):
    """Unicode representation of Service."""
    return self.name
