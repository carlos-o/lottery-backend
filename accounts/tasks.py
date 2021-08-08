from __future__ import absolute_import, unicode_literals
from celery import shared_task
from accounts.models import User
from utils import notifications
from src.base import FRONT_URL
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_verify_account_notification(email: str, activation_code: str):
	"""
		Send an email to the user, to verify your account

		:param email: email of user to activate
		:type email: str
		:param activation_code: code of user to activate
		:type activation_code: str
		:return: True
	"""
	logger.info("OPEN: prepare template to send mail")
	notify = notifications.Notifications(send_email=True, template="email/verify_email.html")
	front_url = FRONT_URL + 'accounts/activate/' + activation_code
	data = {'username': email, "front_url": front_url,  'msg': 'Verify Account'}
	notify.send_email(email_destinity=email, data=data)
	logger.debug("OPEN: email has been send correctly")
	return True
