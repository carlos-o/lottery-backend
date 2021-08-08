from accounts.models import User
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.exceptions import PermissionDenied
from datetime import datetime
from utils.permissions import is_active_user
from utils import services as utils_services
from accounts import validations as accounts_validations
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


def login(data: dict) -> dict:
    """
        Get access to application.
        Raise exception if user or password are incorrect or user does not exist.

        :param data: username and password of user.
        :type data: dict.
        :return: user.
        :raises: ValueError, PermissionDenied.
    """
    username = data.get("username", None)
    password = data.get("password", None)
    logger.debug("Verify: is user data is not empty")
    if username is None or not username:
        logger.error("OPEN:Error username is empty", exc_info=True)
        raise ValueError("The username cannot be empty")
    if password is None or not password:
        logger.error("OPEN:Error password is empty", exc_info=True)
        raise ValueError("The password cannot be empty")
    logger.debug("Verify is user data if correct to provide access")
    try:
        # Obtain user from database if exist
        user = User.objects.get(Q(username=username) | Q(email=username.lower()))
    except Exception as e:
        logger.error("OPEN:Error in petition to login user %s" % str(e), exc_info=True)
        raise ValueError("The username or password is incorrect")
    # Verify is user is active
    if not user.is_active:
        logger.error("OPEN:Error %s accounts is inactive" % user.username, exc_info=True)
        raise PermissionDenied("Account blocked, contact the administrators.")
    # Verify if password match
    if not user.check_password(password):
        logger.error("OPEN:Error %s password doesnot match " % user.username, exc_info=True)
        raise ValueError("The username or password is incorrect")
    logger.debug('OPEN: %s login correctly into API' % user.username)
    user = authenticate(username=user.username, password=password)
    return user


@is_active_user
def logout(user: User) -> bool:
    """
        Remove token access to user into massone-api.
        Raises exception if user is inactive.

        :param user: User into app
        :type: Model User.
        :return: User.
        :raises: ValueError.
    """
    logger.debug("add date to user when he has logout")
    user.last_login = datetime.now()
    user.save()
    logger.debug("remove token access to %s" % user.username)
    user.auth_token.delete()
    logger.debug("OPEN: %s has been logout to app correctly" % user.username)
    return True


def register(data: dict):
    """
        register a user

        :param data: user information
        :return: user
        :raises: ValueError.
    """
    logger.debug("register User")
    email = data.get('email', None)
    if email is None or not email:
        logger.error("OPEN:Error, email is empty")
        raise ValueError("The email field can not be empty")
    accounts_validations.validate_email_exists(data.get('email'))
    validator = accounts_validations.ValidatorRegisterUser(data)
    if validator.validation() is False:
        errors = validator.mistakes()
        for value in errors:
            errors[value] = validator.change_value(errors[value])
        logging.error("ERROR: in information of user %s" % str(errors), exc_info=True)
        raise ValueError(errors)
    try:
        user = User.objects.create(
            username=utils_services.create_username(data.get('first_name'), data.get('last_name')),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=email,
            phone=data.get('phone'),
            address=data.get('address'),
            rut=data.get('rut'),
            gender=data.get('gender'),
            activation=utils_services.code_generator(15),
            password=make_password(utils_services.code_generator(8)),
            is_active=False,
        )
    except Exception as e:
        logging.error("ERROR: to stored user %s" % str(e), exc_info=True)
        raise ValueError("An error occurred while saving the user")
    return user


def activate_account(data: dict):
    """
        activate and add password in user account

        :param data: user information
        :type data: dict
        :return: user
        :raises: ValueError
    """
    user = User.objects.filter(activation=data.get('code')).first()
    if user is not None:
        user.password = make_password(data.get('password'))
        user.is_active = True
        user.activation = None
        user.save()
    else:
        raise ValueError("This code does not belong to you, please contact administrator")
    return user
