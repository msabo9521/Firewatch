# core/tasks.py
from __future__ import absolute_import, unicode_literals
import ipaddress
import celery
from celery import shared_task
from celery.utils.log import get_task_logger
from .backend.snmp_operations import snmp_get
from .backend.mibs import *

from .models import (
    Ipaddresses,
    Credentials,
    Device,
    ObjectID,
)


@shared_task(name="scan")
def scan(pk):
    network = Ipaddresses.objects.get(id=pk)
    ip = network.subnet
    credential = Credentials.objects.get(id=network.credentials.id)
    community = credential.community
    subnet = ipaddress.ip_network(f"{ip}/29")
    ips = []
    for ip in subnet:
        ips.append(str(ip))
    ips = ips[1:-1]
    for net in ips:
        print(net)
        name = snmp_get(net, credential.community, Universal.sysname)
        if name != None:
            description = snmp_get(net, credential.community, Universal.descr)
            objectid = snmp_get(net, credential.community, Universal.objectid)
            pre_uptime = int(snmp_get(net, credential.community, Universal.uptime))*.01
            print(pre_uptime)
            days, remainder = divmod(pre_uptime, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)
            uptime = f"{int(days)} days {int(hours)} hours {int(minutes)} minutes"
            print(objectid)
            sysoid = ObjectID.objects.get(oid=objectid)
            if sysoid.vendor == "Cisco":
                serial = snmp_get(net, credential.community, Cisco.serial)
            if Device.objects.filter(name=name):
                Device.objects.filter(name=name).update(
                    name=name,
                    ip_address=net,
                    manufacturer=sysoid.vendor,
                    type=sysoid.type,
                    device_model=sysoid.model,
                    uptime=uptime,
                    serial=serial,
                    description=description,
                    status=0,

                )
            else:
                p = Device(
                    name=name,
                    ip_address=net,
                    manufacturer=sysoid.vendor,
                    type=sysoid.type,
                    device_model=sysoid.model,
                    uptime=uptime,
                    serial=serial,
                    description=description,
                    status=0,
                )
                p.save()
    print('redis scan is working mother fucker')


