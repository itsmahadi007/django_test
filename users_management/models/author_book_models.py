from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} - {self.name} - {self.date_of_birth}"


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorModel, on_delete=models.RESTRICT, related_name="books")
    published_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    is_archived = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.author.name}"


class BookModelLog(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.SET_NULL, related_name="logs", null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorModel, on_delete=models.RESTRICT, related_name="book_logs")
    action = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.action}"
