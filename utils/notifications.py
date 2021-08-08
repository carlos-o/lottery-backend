from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from src import base as settings
import logging

# inicializate a logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('email')


class Notifications:
    """
        This class contain all method to send email for all notification on system.
    """

    def __init__(self, send_email=True, template=None, template_txt=None):
        """
            Initialize this class with template direction.

            :param send_email: True
            :type send_email: bool.
            :param template: direction of template.
            :type template: string.
        """
        self.template = template
        self.template_txt = template_txt
        self.url_web = settings.URL

    def send_email(self, email_destinity, data):
        """
            This method get the data information and send a email with the template indicate.

            :param email_destinity: email to send information.
            :type email_destinity: string.
            :param data: user information.
            :type data: dict.
        """
        if self.template is None:
            raise ValueError("A template is needed to send an email")
        data["url"] = self.url_web
        subject = data.get('msg')
        logger.info("SUBJECT %s" % subject)
        to = email_destinity
        logger.info("TO %s" % to)
        from_email = settings.EMAIL_HOST_USER
        logger.info("FROM %s" % from_email)
        template = self.template
        template_txt = self.template if self.template_txt is None else self.template_txt
        logger.info("template %s" % template)
        # we replace blank lines for <br> for formatting purposes
        data_html = data.copy()
        html_message = data_html.get('message', '')
        html_message = html_message.replace('\n', '<br>')
        data_html['message'] = html_message
        ###
        text_content = render_to_string(template_txt, data)
        html_content = render_to_string(template, data_html)
        logger.info("send_email_job:data %s" % data)
        logger.info("send_email_job:data_html %s" % data_html)
        ####
        send = EmailMultiAlternatives(subject, text_content, from_email, [to],
                                      headers={'From': 'Lottery <' + from_email + '>',
                                               'Reply-to': 'Lottery <' + from_email + '>'})
        send.attach_alternative(html_content, "text/html")
        send.send()
        return True