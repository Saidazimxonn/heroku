# Generated by Django 3.1 on 2021-02-24 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('specialist', models.CharField(max_length=100, verbose_name='Specialist')),
                ('specialist_en', models.CharField(max_length=100, null=True, verbose_name='Specialist')),
                ('specialist_ru', models.CharField(max_length=100, null=True, verbose_name='Specialist')),
                ('image', models.ImageField(upload_to='uploads', verbose_name='Image')),
                ('info', models.TextField(verbose_name='Info')),
                ('info_en', models.TextField(null=True, verbose_name='Info')),
                ('info_ru', models.TextField(null=True, verbose_name='Info')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('subject_en', models.CharField(max_length=50, null=True, verbose_name='Subject')),
                ('subject_ru', models.CharField(max_length=50, null=True, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('message_en', models.TextField(null=True, verbose_name='Message')),
                ('message_ru', models.TextField(null=True, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your Name', max_length=100, verbose_name='Name')),
                ('name_en', models.CharField(help_text='Your Name', max_length=100, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(help_text='Your Name', max_length=100, null=True, verbose_name='Name')),
                ('email', models.EmailField(help_text='Email Address', max_length=254, verbose_name='Email')),
                ('day', models.CharField(choices=[('day', 'Day'), ('sunday', 'Sunday'), ('monday', 'Monday')], default='D', max_length=10, verbose_name='Day')),
                ('time', models.CharField(choices=[('am', 'AM'), ('pm', 'PM')], default='A', max_length=10, verbose_name='Time')),
                ('message', models.TextField(blank=True, help_text='Your Message...', null=True, verbose_name='Message')),
                ('message_en', models.TextField(blank=True, help_text='Your Message...', null=True, verbose_name='Message')),
                ('message_ru', models.TextField(blank=True, help_text='Your Message...', null=True, verbose_name='Message')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medic.doctor')),
            ],
        ),
    ]
