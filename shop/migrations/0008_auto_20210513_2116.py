

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210513_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default1.jpg', upload_to=''),
        ),
    ]
