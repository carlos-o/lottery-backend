from __future__ import absolute_import, unicode_literals
from celery import shared_task
from accounts.models import User
from utils import notifications
from utils import services
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_winner_notification(email: str):
    """
        send an email to the winning user


        :param email: email of the winner
        :type email: str
        :return: True
    """
    logger.info("OPEN: prepare template to send mail")
    notify = notifications.Notifications(send_email=True, template="email/winner.html")
    data = {'username': email, 'msg': 'Lottery Winner'}
    notify.send_email(email_destinity=email, data=data)
    logger.debug("OPEN: email has been send correctly")
    return True
