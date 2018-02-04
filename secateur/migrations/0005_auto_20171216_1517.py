# Generated by Django 2.0 on 2017-12-16 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secateur', '0004_auto_20171210_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cursor_page_number', models.IntegerField(blank=True, editable=False, null=True)),
                ('from_twitter', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='secateur.Twitter')),
                ('to_twitter', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='secateur.Twitter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='twitter',
            name='blocks2',
            field=models.ManyToManyField(related_name='blocked_by2', through='secateur.Block', to='secateur.Twitter'),
        ),
    ]
