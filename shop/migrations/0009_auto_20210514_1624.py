

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210513_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(related_name='item', to='shop.Category'),
        ),
    ]
