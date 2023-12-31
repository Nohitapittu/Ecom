# Generated by Django 4.2.7 on 2023-11-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ecomapp', '0002_remove_post_user_delete_comment_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
