# Generated by Django 4.2.7 on 2023-11-18 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fads',
            name='decade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.decades'),
        ),
    ]
