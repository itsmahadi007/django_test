from datetime import datetime

from django_filters import rest_framework as filters

from users_management.models import BookModel


class BookModelFilter(filters.FilterSet):
    title = filters.CharFilter(method="filter")
    author = filters.CharFilter(method="filter")
    author_name = filters.CharFilter(method="filter")
    genre = filters.CharFilter(method="filter")
    published_date_range = filters.CharFilter(method="filter")

    class Meta:
        model = BookModel
        fields = [
            "id",
            "title",
            "author",
            "author_name",
            "genre",
            "published_date_range",
            "is_archived"
        ]

    @staticmethod
    def filter(queryset, name, value):
        if name == "title":
            return queryset.filter(title__icontains=value)
        elif name == "author":
            return queryset.filter(author_id=value)
        elif name == "author_name":
            return queryset.filter(author__name__icontains=value)
        elif name == "genre":
            return queryset.filter(genre__icontains=value)
        elif name == "published_date_range":
            # Example value = "2021-01-01,2021-12-31"
            start_date_str, end_date_str = [s.strip() for s in value.split(",")]
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
            data = queryset.filter(
                published_date_range__range=(start_date, end_date)
            )
            return data
        else:
            return queryset
