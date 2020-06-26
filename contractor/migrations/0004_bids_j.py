# Generated by Django 3.0.7 on 2020-06-26 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_jobs_fragile'),
        ('contractor', '0003_auto_20200625_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='j',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='user.Jobs'),
        ),
    ]
