

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210513_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title', unique=True, verbose_name='url'),
        ),
    ]
