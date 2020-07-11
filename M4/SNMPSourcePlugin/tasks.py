from celery import shared_task
from easysnmp import snmp_get
from pprint import pprint


@shared_task(bind=True, name='snmp_source')
def snmp_source(self, oid, version, datatype, datasource):
    # do snmp get here
    # pprint(vars(self))
    res = str(snmp_get(oid, hostname=datasource, community='public', version=int(version)).value)
    return res