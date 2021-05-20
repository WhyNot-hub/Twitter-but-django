

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200810_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postrate',
            name='liked',
            field=models.BooleanField(null=True),
        ),
    ]
