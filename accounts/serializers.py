import serpy


class UserSerializer(serpy.Serializer):
	id = serpy.Field()
	first_name = serpy.Field()
	last_name = serpy.Field()
	email = serpy.Field()
