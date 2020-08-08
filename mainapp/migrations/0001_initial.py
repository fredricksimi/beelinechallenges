# Generated by Django 3.0.7 on 2020-07-09 09:47

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeAudience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChallengeTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Preapproved_challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('external_url', models.CharField(default='', max_length=150)),
                ('length', models.CharField(max_length=150)),
                ('short_description', models.TextField()),
                ('steps_to_complete', models.TextField()),
                ('why', models.TextField(blank=True, null=True)),
                ('tips', models.TextField(blank=True, null=True)),
                ('tags', models.ManyToManyField(to='mainapp.ChallengeTag')),
            ],
        ),
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('offered_by', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, default='default-banner.jpg', upload_to='media_pics/')),
                ('challenge_summary', models.CharField(default='', max_length=250)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('external_website_url', models.CharField(default='', max_length=150)),
                ('participate_link', models.CharField(default='', max_length=200)),
                ('who_can_participate', ckeditor_uploader.fields.RichTextUploadingField()),
                ('how_to_participate', ckeditor_uploader.fields.RichTextUploadingField()),
                ('prize', models.CharField(help_text='Include the currency and amount in this field', max_length=150)),
                ('additional_information', ckeditor_uploader.fields.RichTextUploadingField()),
                ('point_of_contact', models.TextField()),
                ('date_posted', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('open_until', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Coming Soon', 'Coming Soon'), ('Archived', 'Archived'), ('Rolling', 'Rolling')], default='Open', max_length=200)),
                ('tags', models.ManyToManyField(to='mainapp.ChallengeTag')),
                ('targeted_audience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ChallengeAudience')),
            ],
            options={
                'verbose_name': 'challenge',
                'verbose_name_plural': 'challenges',
            },
        ),
    ]
