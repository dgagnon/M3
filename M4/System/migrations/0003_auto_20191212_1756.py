# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-12 22:56
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    FrontEnd = apps.get_model('System', 'FrontEnd')
    # PluginPoint = apps.get_model('djangoplugins', 'PluginPoint')
    Plugin = apps.get_model('djangoplugins', 'Plugin')
    SourcePlugin = apps.get_model("System", "SourcePlugin")
    HookPlugin = apps.get_model("System", "HookPlugin")
    DisplayPlugin = apps.get_model("System", "DisplayPlugin")
    TriggerPlugin = apps.get_model("System", "TriggerPlugin")
    Asset = apps.get_model("System", "Asset")
    Datapoint = apps.get_model("System", "Datapoint")
    SLA = apps.get_model("System", "Sla")
    CF = apps.get_model("System", "CustomField")
    db_alias = schema_editor.connection.alias

    # PluginPoint.objects.using(db_alias).create(pythonpath='M4.System.FrontEndPlugin', title='DashboardPlugin', status=0)
    # Plugin.objects.using(db_alias).create(point=PluginPoint.objects.using(db_alias).get(title='DashboardPlugin'),
    #                                       pythonpath='M4.DashboardDisplayPlugin.plugins.DefaultDashboardFrontEnd',
    #                                       title='Default Dashboard', name='dashboard', index=0, status=0)

    FrontEnd.objects.using(db_alias).create(pk=1, name='dashboard', title='Default Dashboard',
                                            plugin=Plugin.objects.using(db_alias).get(name='dashboard'))

    Datapoint.objects.using(db_alias).create(pk=1, name='my-local-test', title='My Local Test', datatype='number',
                                             source=SourcePlugin.objects.using(db_alias).get(id=1),
                                             trigger=TriggerPlugin.objects.using(db_alias).get(id=1, datatype='number'),
                                             hook=HookPlugin.objects.using(db_alias).get(id=1),
                                             display=DisplayPlugin.objects.using(db_alias).get(id=1))

    myAsset = Asset.objects.using(db_alias).create(pk=1, name='my-first-asset', title='My First Asset')
    myAsset.datapoints = Datapoint.objects.using(db_alias).filter(pk=1)
    myAsset.save()

    SLA.objects.using(db_alias).create(pk=1, name='my-first-sla', title='My First SLA')
    mySLA = SLA.objects.using(db_alias).get(pk=1)
    mySLA.datapoints = Datapoint.objects.using(db_alias).filter(pk=1)
    mySLA.assets = Asset.objects.using(db_alias).filter(pk=1)

    CF.objects.using(db_alias).create(id=1, name='owner', content='local admin', object_id=1, content_type_id=9)
    CF.objects.using(db_alias).create(id=2, name='link-to-doc', content='https://m4system.com', object_id=1,
                                      content_type_id=16)
    CF.objects.using(db_alias).create(id=3, name='stakeholder', content='local admin', object_id=1,
                                      content_type_id=18)


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    FrontEnd = apps.get_model('System', 'FrontEnd')
    # Plugin = apps.get_model('djangoplugins', 'Plugin')
    # PluginPoint = apps.get_model('djangoplugins', 'PluginPoint')
    Datapoint = apps.get_model("System", "Datapoint")
    Asset = apps.get_model("System", "Asset")
    SLA = apps.get_model("System", "SLA")
    CF = apps.get_model("System", "CustomField")
    db_alias = schema_editor.connection.alias

    FrontEnd.objects.using(db_alias).get(pk=1).delete()
    # Plugin.objects.using(db_alias).get(name='dashboard').delete()
    # PluginPoint.objects.using(db_alias).get(title='DashboardPlugin').delete()
    Datapoint.objects.using(db_alias).get(pk=1).delete()
    Asset.objects.using(db_alias).get(pk=1).delete()
    SLA.objects.using(db_alias).get(pk=1).delete()
    CF.objects.using(db_alias).get(pk=1).delete()
    CF.objects.using(db_alias).get(pk=2).delete()
    CF.objects.using(db_alias).get(pk=3).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('System', '0002_auto_20191212_1739'),
        ('djangoplugins', '0001_initial'),
        ('ThresholdTriggerPlugin', '0002_auto_20191212_1728'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]