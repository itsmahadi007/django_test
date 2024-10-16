from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from users_management.models import BookModelLog, BookModel


@receiver(post_save, sender=BookModel)
def book_model_created(sender, instance, **kwargs):
    # Check if the instance is just created
    if kwargs.get("created", True):
        # on created instance, create a log
        BookModelLog.objects.create(
            book=instance,
            title=instance.title,
            author=instance.author,
            action="created",
        )
# on deleted instance, create a log
@receiver(pre_delete, sender=BookModel)
def book_model_deleted(sender, instance, **kwargs):
    BookModelLog.objects.create(
        book=instance,
        title=instance.title,
        author=instance.author,
        action="deleted",
    )
