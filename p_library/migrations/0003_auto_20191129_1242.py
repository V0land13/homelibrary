# Generated by Django 2.2.7 on 2019-11-29 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('p_library', '0002_book_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(choices=[('New member', 'Новичек'), ('Silver', 'Серебро'), ('Gold', 'Золото'), ('Platinum', 'Платина')], max_length=15, verbose_name='Уровень клубной карты')),
                ('age', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='booksrent',
            name='book_renter',
            field=models.OneToOneField(blank=True, help_text='Помните, что 1 пользователь может взять 1 книгу!', null=True, on_delete=django.db.models.deletion.PROTECT, to='p_library.Reader', verbose_name='Арендатор'),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
