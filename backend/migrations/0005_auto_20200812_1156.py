

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200812_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_text',
            new_name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='in_reply_to_post',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
