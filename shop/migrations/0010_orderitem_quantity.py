

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210514_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
