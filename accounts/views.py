from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import (
	permissions,
	status
)
from rest_framework.response import Response
from accounts import (
	services as accounts_services,
	tasks as accounts_tasks,
	serializers as accounts_serializers
)
from utils.response import ResponseDetail
from django.core.exceptions import PermissionDenied
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


class LoginView(APIView):
	permission_classes = (permissions.AllowAny,)

	def post(self, request):
		logger.info("Make authentication to API")
		try:
			user = accounts_services.login(request.data)
		except ValueError as e:
			logger.error("ValueError: %s" % str(e), exc_info=True)
			return Response(
				{"detail": ResponseDetail().errors_detail(code=400, message="ValueError", error=str(e))},
				status=status.HTTP_400_BAD_REQUEST)
		except PermissionDenied as e:
			logger.error("PermissionError: %s" % str(e), exc_info=True)
			return Response(
				{"detail": ResponseDetail().errors_detail(code=401, message="PermissionError", error=str(e))},
				status=status.HTTP_401_UNAUTHORIZED)
		except Exception as e:
			logger.error("Exception: INTERNAL SERVER ERROR %s" % str(e), exc_info=True)
			return Response(
				{"detail": ResponseDetail().errors_detail(error={"error": [str(e)]})},
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = accounts_serializers.UserSerializer(user, many=False).data
		token, created = Token.objects.get_or_create(user=user)
		serializer['token'] = token.key
		return Response({"detail": ResponseDetail().success_detail(data=serializer)}, status=status.HTTP_200_OK)


class LogoutView(APIView):
	"""
		Deletes the user's token in the system.
	"""
	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request):
		logger.info("Logout from the API")
		print(request.user)
		try:
			accounts_services.logout(user=request.user)
		except ValueError as e:
			return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except PermissionDenied as e:
			return Response({"detail": str(e)}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		return Response({"detail": ResponseDetail().success_detail()}, status=status.HTTP_200_OK)


class RegisterUserView(APIView):
	permission_classes = (permissions.AllowAny,)

	def post(self):
		return Response({})

	def get(self):
		return Response({})
