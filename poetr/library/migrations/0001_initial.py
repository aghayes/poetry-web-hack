# Generated by Django 3.1.4 on 2020-12-05 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_title', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text='enter poem title', max_length=48)),
                ('text', models.CharField(help_text='enter poem text', max_length=280)),
                ('author', models.CharField(help_text='enter author', max_length=48)),
                ('genres', models.ManyToManyField(blank=True, to='library.Genre')),
                ('links', models.ManyToManyField(blank=True, related_name='_poem_links_+', to='library.Poem')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_timestamp', models.DateTimeField(auto_now_add=True)),
                ('report_text', models.CharField(help_text='describe why you are reporting this poem', max_length=400)),
                ('report_type', models.CharField(choices=[('nsfw', 'NSFW'), ('hrmt', 'HARASSMENT'), ('cprt', 'COPYRIGHT')], default='cprt', max_length=4)),
                ('report_poem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='library.poem')),
            ],
        ),
    ]