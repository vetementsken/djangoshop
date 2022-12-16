
import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title', unique=True, verbose_name='url'),
        ),
    ]
