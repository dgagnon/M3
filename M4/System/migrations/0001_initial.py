# Generated by Django 3.0.6 on 2020-05-29 02:41

from django.db import migrations, models
import django.db.models.deletion
import djangoplugins.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djangoplugins', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(blank=True, help_text='Internal name for the Asset.', max_length=64, unique=True, verbose_name='Asset Name')),
                ('title', models.CharField(help_text='Verbose name for display purposes', max_length=256, verbose_name='Asset Title')),
            ],
            options={
                'verbose_name': 'Asset',
                'verbose_name_plural': 'Assets',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Datapoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(blank=True, help_text='Internal name for the Datapoint.', max_length=64, unique=True, verbose_name='Datapoint Name')),
                ('title', models.CharField(help_text='Verbose name for display purposes', max_length=256, verbose_name='Datapoint Title')),
                ('datatype', models.CharField(choices=[('number', 'Number'), ('string', 'Character String'), ('boolean', 'Booleans')], default='string', help_text='The internal type for this datapoint.', max_length=8, verbose_name='Data type')),
            ],
            options={
                'verbose_name': 'Data Point',
                'verbose_name_plural': 'Data Points',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(help_text='Setting name', max_length=64, unique=True, verbose_name='Name')),
                ('value', models.CharField(help_text='Setting value', max_length=1024, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
                'ordering': ['-key'],
            },
        ),
        migrations.CreateModel(
            name='TriggerPlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(verbose_name='Name')),
                ('datatype', models.CharField(choices=[('number', 'Number'), ('string', 'Character String'), ('boolean', 'Booleans')], default='string', help_text='The data datatype this trigger supports.', max_length=8, verbose_name='Data type')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='SourcePlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(verbose_name='Name')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Sla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(blank=True, help_text='Internal name for the SLA.', max_length=64, unique=True, verbose_name='SLA Name')),
                ('title', models.CharField(help_text='Verbose name for display purposes', max_length=256, verbose_name='SLA Title')),
                ('assets', models.ManyToManyField(help_text='Assets assigned to this SLA.', to='System.Asset', verbose_name='Assigned Assets')),
                ('datapoints', models.ManyToManyField(help_text='Datapoints assigned to this SLA.', to='System.Datapoint', verbose_name='Assigned Assets')),
            ],
            options={
                'verbose_name': 'SLA',
                'verbose_name_plural': 'SLAs',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='HookPlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(verbose_name='Name')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Frontend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(blank=True, help_text='Internal name for the frontend.', max_length=64, unique=True, verbose_name='Name')),
                ('title', models.CharField(help_text='Verbose name for display purposes.', max_length=256, verbose_name='Title')),
                ('plugin', djangoplugins.fields.PluginField(limit_choices_to={'point__pythonpath': 'M4.System.plugins.FrontEndPlugin'}, on_delete=django.db.models.deletion.CASCADE, to='djangoplugins.Plugin')),
            ],
            options={
                'verbose_name': 'Front-End',
                'verbose_name_plural': 'Front-Ends',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='DisplayPlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(verbose_name='Name')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='datapoint',
            name='display',
            field=models.ForeignKey(blank=True, help_text='Select the plugin configuration that will be used to display this datapoint on the frontends. If the list is empty, it means you need to create a plugin configuration first.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='display', to='System.DisplayPlugin', verbose_name='Display Plugin'),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='hook',
            field=models.ForeignKey(blank=True, help_text='Select the plugin configuration that will be executed when the status of the datapoint changes. If the list is empty, it means you need to create a plugin configuration first.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hook', to='System.HookPlugin', verbose_name='Hook Plugin'),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='source',
            field=models.ForeignKey(help_text='Select the plugin configuration that will be used to source the data for this datapoint. If the list is empty, it means you need to create a plugin configuration first.', on_delete=django.db.models.deletion.CASCADE, related_name='source', to='System.SourcePlugin', verbose_name='Source Plugin'),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='trigger',
            field=models.ForeignKey(blank=True, help_text='Select the plugin configuration that will be used to decide if the datapoint is failing. If the list is empty, it means you need to create a plugin configuration first.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trigger', to='System.TriggerPlugin', verbose_name='Trigger Plugin'),
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(verbose_name='Name')),
                ('content', models.CharField(max_length=4096, verbose_name='Content')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Custom Field',
                'verbose_name_plural': 'Custom Fields',
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='datapoints',
            field=models.ManyToManyField(blank=True, help_text='Assign datapoints to assets here.  You can then assign an SLA and start monitoring availibility.', to='System.Datapoint', verbose_name='Datapoints which link to this assets.'),
        ),
    ]