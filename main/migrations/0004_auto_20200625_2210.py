# Generated by Django 3.0.7 on 2020-06-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200528_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.CharField(choices=[('Imikino', 'Imikino'), ('Imyidagaduro', 'Imyidagaduro'), ('Politiki', 'Politiki'), ('Ikoranabuhanga', 'Ikoranabuhanga'), ('Ubuzima', 'Ubuzima'), ('Sobanukirwa', 'Sobanukirwa')], default='Amakuru', max_length=100),
        ),
    ]
