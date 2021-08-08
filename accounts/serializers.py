import serpy


class UserSerializer(serpy.Serializer):
	id = serpy.Field()
	# is_active = serpy.Field()
	email = serpy.Field()

