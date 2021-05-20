
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200811_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comment_text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='posted_by',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Publication Date'),
        ),
    ]
