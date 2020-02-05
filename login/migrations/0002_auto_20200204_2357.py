# Generated by Django 2.2.9 on 2020-02-04 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citycode', models.CharField(max_length=6, verbose_name='Abbr')),
                ('cityname', models.CharField(max_length=30, verbose_name='Cityname(English)')),
                ('citycname', models.CharField(max_length=30, verbose_name='Cityname(Chinese)')),
                ('displayseq', models.SmallIntegerField(unique=True, verbose_name='显示顺序')),
                ('other1', models.CharField(blank=True, max_length=200, null=True, verbose_name='预留字段1')),
                ('other2', models.CharField(blank=True, max_length=200, null=True, verbose_name='预留字段2')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'City',
                'ordering': ['displayseq'],
            },
        ),
        migrations.CreateModel(
            name='Merchantclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memclass', models.SmallIntegerField(default=1, unique=True, verbose_name='ClassCode')),
                ('memclassname', models.CharField(default='blue', max_length=30, verbose_name='Class(English)')),
                ('memclasscname', models.CharField(default='蓝卡', max_length=30, verbose_name='Class(Chinese)')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Class Description')),
            ],
            options={
                'verbose_name': 'Merchant Class',
                'verbose_name_plural': 'Merchant Class',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procode', models.CharField(max_length=6, verbose_name='Abbr')),
                ('provincename', models.CharField(max_length=50, verbose_name='Province(English)')),
                ('provincecname', models.CharField(max_length=30, verbose_name='Province(Chinese)')),
                ('displayseq', models.SmallIntegerField(unique=True, verbose_name='Display Sequence')),
                ('other1', models.CharField(blank=True, max_length=200, null=True, verbose_name='预留字段1')),
                ('other2', models.CharField(blank=True, max_length=200, null=True, verbose_name='预留字段2')),
            ],
            options={
                'verbose_name': 'Province',
                'verbose_name_plural': 'Province',
                'ordering': ['provincename'],
            },
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchantid', models.CharField(max_length=30, unique=True, verbose_name='Userid')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
                ('companyname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Company Name')),
                ('contactperson', models.CharField(blank=True, max_length=50, null=True, verbose_name='Contact')),
                ('phoneno', models.CharField(max_length=30, verbose_name='Phone Number')),
                ('address', models.CharField(max_length=90, verbose_name='Address')),
                ('postcode', models.CharField(max_length=20, verbose_name='Postcode')),
                ('wechatid', models.CharField(blank=True, max_length=50, null=True, verbose_name='Wechat')),
                ('emailaddr', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('regdate', models.DateField(auto_now=True, verbose_name='Register Date')),
                ('merchantscore', models.IntegerField(default=0, verbose_name='Scores')),
                ('merchantstatus', models.SmallIntegerField(choices=[(1, 'ON'), (2, 'OFF')], default=1, verbose_name='Status')),
                ('systemstatus', models.SmallIntegerField(choices=[(1, 'Allow'), (2, 'Forbid')], default=1, verbose_name='System Status')),
                ('merchantintro', models.TextField(blank=True, null=True, verbose_name='Introduction')),
                ('other1', models.CharField(blank=True, max_length=200, null=True, verbose_name='预留字段1')),
                ('other2', models.CharField(blank=True, max_length=200, null=True, verbose_name='预留字段2')),
                ('other3', models.CharField(blank=True, max_length=200, null=True, verbose_name='预留字段3')),
                ('other4', models.CharField(blank=True, max_length=200, null=True, verbose_name='预留字段4')),
                ('other5', models.CharField(blank=True, max_length=200, null=True, verbose_name='预留字段5')),
                ('citycode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.City', verbose_name='City')),
                ('merchantclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Merchantclass', verbose_name='Class')),
                ('procode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Province', verbose_name='Province')),
            ],
            options={
                'verbose_name': 'Merchant',
                'verbose_name_plural': 'Merchant',
                'ordering': ['merchantid'],
            },
        ),
        migrations.AddField(
            model_name='city',
            name='procode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Province', verbose_name='Belong to'),
        ),
        migrations.AddIndex(
            model_name='merchant',
            index=models.Index(fields=['regdate'], name='regdate_idx'),
        ),
    ]
