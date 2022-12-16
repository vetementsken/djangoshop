

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='characteristics',
            field=django_ckeditor_5.fields.CKEditor5Field(default=1, verbose_name='Characteristics'),
            preserve_default=False,
        ),
    ]
