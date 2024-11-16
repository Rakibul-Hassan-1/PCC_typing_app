# Generated by Django 5.1.1 on 2024-11-15 11:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typing_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='typingcontext',
            old_name='submitted_at',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='typingcontext',
            name='score',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='TypingContest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_id', models.IntegerField()),
                ('wpm', models.FloatField()),
                ('accuracy', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
