from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

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
