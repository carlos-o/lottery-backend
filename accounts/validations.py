from cerberus import Validator
from django.utils.translation import gettext as _
from accounts.models import User
import re
import logging

# inicializate a logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def validate_email(email):
	"""
		Check if the email is correct

		:param email: email of user massone
		:return: True
		:raises: ValueError
	"""
	if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
		raise ValueError(str(_("Please enter a valid email address")))
	if len(email.split("@")[0]) >= 64:
		raise ValueError(str(_("Invalid email")))
	if len(email.split("@")[1].split(".")[0]) >= 255:
		raise ValueError(str(_("Invalid email")))
	return True


def validate_email_exists(email: str):
	"""
		Method to verify if email of user exists in massone-api
		The email is unique

		:param email: email of user massone
		:type email: str
		:return: bool
		:raises: ValueError
	"""
	logger.info("VALIDATE: if email exist in database")
	if User.objects.filter(email=email.lower()).exists():
		logging.error("ERROR: email exist %s" % email)
		raise ValueError("Email registered please try with another")
	return True


class ValidatorRegisterUser(Validator):
	"""
		Validate class to register account.
	"""

	schema = {
		'first_name': {'type': 'string', 'required': True, 'empty': False, 'minlength': 3, 'maxlength': 30},
		'last_name': {'type': 'string', 'required': True, 'empty': False, 'minlength': 3, 'maxlength': 30},
		'email': {'type': 'string', 'required': True, 'empty': False, "mail": True, 'nullable': True},
		'phone': {'type': 'string', 'required': True, 'empty': False, 'regex': '^[0-9]+', 'minlength': 7, 'maxlength': 16},
		'address': {'type': 'string', 'required': True, 'empty': False, 'maxlength': 255},
		'rut': {'type': 'string', 'required': True, 'empty': False},
		'gender': {'type': 'string', 'required': True, 'empty': False}
	}

	def __init__(self, data, *args, **kwargs):
		"""
			initialize cerberus with the user information to register in weedmatch.

			:param data: user information.
			:type data: dict.
		"""
		super(ValidatorRegisterUser, self).__init__(*args, **kwargs)
		self.data = data
		self.schema = self.__class__.schema

	def validation(self):
		"""
			:return: none if data is correct
		"""
		return self.validate(self.data, self.schema)

	def _validate_mail(self, mail, field, value):
		""" Validate the user's email

		The rule's arguments are validated against this schema:
		{'type': 'boolean'}
		"""
		if mail and value:
			if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', value):
				self._error(field, str(_("Please enter a valid email address")))
			elif len(value.split("@")[0]) >= 64:
				self._error(field, str(_("Invalid email")))
			elif len(value.split("@")[1].split(".")[0]) >= 255:
				self._error(field, str(_("Invalid email")))

	def change_value(self, data: list) -> list:
		"""
			this method covers all cerberus error messages from English to Spanish,
			depends on the Accept-Language header.

			:param data: error messages of cerberus.
			:return: list with error messages.
		"""
		for i in range(0, len(data)):
			if data[i][0:15] == "unallowed value":
				convert = str(data[i])
				data[i] = str(_(convert[0:15])) + convert[15:]
			elif data[i][:26] == "value does not match regex":
				convert = str(data[i])
				data[i] = str(_(data[i][:26]))
			else:
				convert = str(data[i])
				data[i] = str(_(convert))
		return data

	def mistakes(self):
		"""
			This method returns the error when, the information sent by the user does not comply
			with the rules in the validation with cerberus

			:return: error of cerberus
		"""
		return self.errors
