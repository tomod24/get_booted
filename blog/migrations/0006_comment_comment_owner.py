# Generated by Django 3.1.5 on 2021-01-29 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20210128_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_owner',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='comment_owner', to='auth.user'),
            preserve_default=False,
        ),
    ]