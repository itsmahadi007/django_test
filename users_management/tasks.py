from datetime import datetime, timedelta

from celery import shared_task  # Used to mark a function as a Celery task
from celery.utils.log import get_task_logger  # Used to log task information

from users_management.models import BookModel

logger = get_task_logger(__name__)


@shared_task(name='users_management.tasks.check_old_book')
def check_old_book():
    print('Checking old books')
    # Get all books published more than 10 years ago and mark them as archived
    books = BookModel.objects.filter(
        published_date__lte=datetime.now() - timedelta(days=365 * 10)
    )
    books.update(is_archived=True)

    print('Old books checked')
