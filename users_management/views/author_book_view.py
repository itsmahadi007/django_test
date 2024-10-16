from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from users_management.filters.filters import BookModelFilter
from users_management.models import BookModel, AuthorModel

from users_management.serializers.model_serializers import BookModelSerializerDetails, BookModelSerializer, \
    AuthorModelSerializer, AuthorModelSerializerDetails


class BookModelViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookModelFilter

    serializer_classes = {
        "list": BookModelSerializerDetails,
        "retrieve": BookModelSerializerDetails,
        "create": BookModelSerializer,
        "update": BookModelSerializer,
    }

    default_serializer_class = BookModelSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        queryset = BookModel.objects.select_related("author").all()
        return queryset

    cache_response_timeout = 60 * 60


class AuthorModelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    serializer_classes = {
        "list": AuthorModelSerializerDetails,
        "retrieve": AuthorModelSerializerDetails,
        "create": AuthorModelSerializer,
        "update": AuthorModelSerializer,
    }

    default_serializer_class = BookModelSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        queryset = AuthorModel.objects.prefetch_related("books").all()
        return queryset
