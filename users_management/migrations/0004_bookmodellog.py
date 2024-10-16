# Generated by Django 4.2 on 2024-10-16 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_management', '0003_bookmodel_is_archived'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookModelLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_logs', to='users_management.authormodel')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='users_management.bookmodel')),
            ],
        ),
    ]