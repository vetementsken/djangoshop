

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210513_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=autoslug.fields.AutoSlugField(max_length=255, unique=True, verbose_name='url'),
        ),
    ]
