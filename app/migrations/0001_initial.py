# Generated by Django 2.0.3 on 2018-07-10 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('unreach_reason', models.CharField(blank=True, max_length=128)),
                ('type', models.CharField(blank=True, max_length=128)),
                ('family', models.CharField(blank=True, max_length=128)),
                ('device_id', models.CharField(blank=True, max_length=128)),
                ('hostname', models.CharField(blank=True, max_length=128)),
                ('ip', models.GenericIPAddressField()),
                ('config', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'All devices',
                'verbose_name': 'All devices',
                'db_table': 'device',
            },
        ),
        migrations.CreateModel(
            name='IssueLogMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('reject_msg', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Issue messages',
                'verbose_name': 'Issue log messages',
                'db_table': 'issue_log_message',
            },
        ),
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('user_name', models.CharField(blank=True, max_length=128)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('service_ticket', models.CharField(blank=True, max_length=128)),
                ('mttr', models.DurationField(blank=True, null=True)),
                ('mttri', models.DurationField(blank=True, null=True)),
                ('service_availability', models.PositiveSmallIntegerField(default=0)),
                ('customer_satisfaction', models.PositiveSmallIntegerField(default=0)),
                ('bot_token', models.CharField(blank=True, max_length=128)),
                ('current', models.BooleanField(default=True)),
                ('webex_room_id', models.CharField(blank=True, max_length=128)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.NetType')),
            ],
            options={
                'verbose_name_plural': 'Existing networks',
                'verbose_name': 'Existing networks',
                'db_table': 'network',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=64)),
                ('second_name', models.CharField(blank=True, max_length=64)),
                ('full_name', models.CharField(blank=True, max_length=128)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Role')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='issuelogmessage',
            name='decision_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.UserProfile'),
        ),
        migrations.AddField(
            model_name='issuelogmessage',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Device'),
        ),
        migrations.AddField(
            model_name='issuelogmessage',
            name='issue_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.IssueType'),
        ),
        migrations.AddField(
            model_name='issuelogmessage',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Status'),
        ),
        migrations.AddField(
            model_name='device',
            name='network',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Network'),
        ),
    ]
