from rest_framework import serializers

from users_management.models import AuthorModel, BookModel


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = "__all__"


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = "__all__"


class BookModelSerializerDetails(serializers.ModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = BookModel
        fields = "__all__"


class AuthorModelSerializerDetails(serializers.ModelSerializer):
    books = BookModelSerializer(many=True)

    class Meta:
        model = AuthorModel
        fields = "__all__"
