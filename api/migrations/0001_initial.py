# Generated by Django 3.2.7 on 2021-11-21 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'naga_shop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AlertTbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_msg', models.CharField(max_length=255)),
                ('alert_time', models.DateTimeField(auto_now_add=True, verbose_name='경고 방송 송출 시간')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shop')),
            ],
            options={
                'db_table': 'naga_alert',
                'ordering': ('-alert_time',),
            },
        ),
    ]
