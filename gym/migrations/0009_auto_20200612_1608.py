# Generated by Django 2.2.6 on 2020-06-12 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0008_dietplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=200, null=True)),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('book_date', models.CharField(max_length=30, null=True)),
                ('total', models.IntegerField(null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Member')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Status')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Member')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Product')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='product',
        ),
        migrations.RemoveField(
            model_name='tempcart',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
        migrations.DeleteModel(
            name='TempCart',
        ),
    ]
