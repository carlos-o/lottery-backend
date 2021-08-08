import random
import string
from accounts.models import User

def get_url(url: str):
    """
        Method get url from pagination

        :param url: url of next or previous
        :type url: str
        :return: url
    """
    count = 0
    position = 0
    # capture position of chart /
    for i, chart in enumerate(url):
        if "/" == chart:
            position = i
            count = count + 1
        if count > 2:
            break
    # get temporal url
    temporal_url = url[position:]
    return temporal_url


def code_generator(size=8, chars=string.ascii_uppercase + string.digits):
    """
       this method generates a string randomly

       :param size: size of string.
       :type size: integer.
       :param chars: sting with number and character
       :type chars: str.
       :return: random string.
    """
    return ''.join(random.choice(chars) for _ in range(size))


def create_username(first_name: str, last_name: str):
    """
        Method to create username with name of user

        :param first_name: first_name of user
        :type first_name: str
        :param last_name: last_name of user
        :type last_name: str
        :return: name without white space
    """
    user_name = first_name + last_name
    random_number = str(random.randint(0, 999))
    if len(random_number) == 2:
        random_number = '0' + random_number
    if len(random_number) == 1:
        random_number = '00' + random_number
    user_name = user_name + '_' + random_number
    if User.objects.filter(username=user_name).exists():
        return create_username(first_name, last_name)
    return user_name
