from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
	"""
		the model class to store all user information.
	"""
	SEX_MALE = "Male"
	SEX_FEMALE = "Female"
	SEX_OTHER = "Other"
	TYPE_GENDER = (
		(SEX_MALE, _('Male')),
		(SEX_FEMALE, _('Female')),
		(SEX_OTHER, _("Other"))
	)
	activation = models.CharField(_('Activation'), max_length=15, blank=True, null=True)
	phone = models.CharField(_('Phone Number'), max_length=16, blank=True, null=True)
	address = models.CharField(_('address'), max_length=255, blank=True, null=True)
	rut = models.CharField(_('Rut'), max_length=15, blank=True, null=True)
	gender = models.CharField(_('Type Gender'), max_length=10, choices=TYPE_GENDER, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	deleted_at = models.DateTimeField(blank=True, null=True)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.username
