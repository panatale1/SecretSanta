# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcludedPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('address_1', models.CharField(blank=True, max_length=50, null=True)),
                ('address_2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('phone', models.CharField(blank=True, max_length=14, null=True)),
                ('extension', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SantaRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='santa', to='secretsanta.Person')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretsanta.Person')),
            ],
        ),
        migrations.AddField(
            model_name='excludedpeople',
            name='excluded',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretsanta.Person'),
        ),
        migrations.AddField(
            model_name='excludedpeople',
            name='this_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excluded', to='secretsanta.Person'),
        ),
    ]