

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_item_characteristics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
