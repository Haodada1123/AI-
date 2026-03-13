# Generated manually to add update_time

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="update_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
