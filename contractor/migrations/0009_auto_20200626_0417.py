# Generated by Django 3.0.7 on 2020-06-26 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_completedjobs'),
        ('contractor', '0008_auto_20200626_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='j',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='user.Jobs'),
        ),
    ]
