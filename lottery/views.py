from rest_framework.views import APIView
from rest_framework import (
	permissions,
	status
)
from rest_framework.response import Response
from lottery import (services as lottery_services, tasks as lottery_tasks)
from accounts import serializers as accounts_serializers
from utils.response import ResponseDetail
from utils.pagination import CustomPagination
from django.core.exceptions import PermissionDenied
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


class ParticipantsView(APIView):

	permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

	def get(self, request):
		logger.info("get list with all lottery participants")
		try:
			participants = lottery_services.participants(user=request.user)
		except Exception as e:
			logger.error("Exception: INTERNAL SERVER ERROR %s" % str(e), exc_info=True)
			return Response(
				{"detail": ResponseDetail().errors_detail(error={"error": [str(e)]})},
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		paginator = CustomPagination()
		context = paginator.paginate_queryset(participants, request)
		serializer = accounts_serializers.UserSerializer(context, many=True).data
		return paginator.get_paginated_response(serializer)


class LotteryRunView(APIView):

	permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

	def get(self, request):
		logger.info("run lottery and get the winner")
		try:
			winner = lottery_services.run_lottery(user=request.user)
		except Exception as e:
			logger.error("Exception: INTERNAL SERVER ERROR %s" % str(e), exc_info=True)
			return Response(
				{"detail": ResponseDetail().errors_detail(error={"error": [str(e)]})},
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = accounts_serializers.UserSerializer(winner, many=False).data
		lottery_tasks.send_winner_notification.delay(serializer['email'])
		return Response(
			{"detail": ResponseDetail().success_detail(data=serializer, message="Winner")},
			status=status.HTTP_200_OK)
