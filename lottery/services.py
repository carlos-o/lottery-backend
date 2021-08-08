from accounts.models import User
from random import choice


def participants(user: User) -> list:
	"""
		obtain all participants registered

		:param user: User admin
		:type: Model User.
		:return: all participants registered.
	"""
	participant_users = User.objects.filter(is_staff=False, is_active=True)
	return participant_users


def run_lottery(user: User) -> dict:
	"""
		obtain the winner of lottery

		:param user: User admin
		:type: Model User.
		:return: User
	"""
	winner = choice(User.objects.filter(is_staff=False, is_active=True))
	return winner
