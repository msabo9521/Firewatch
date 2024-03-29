import ipaddress, time
import threading
from pysnmp.hlapi import *

addresses = '10.69.250.0/24'
community = 'sabonetro'
subnet = ipaddress.ip_network(addresses)
ips = []
for ip in subnet:
    ips.append(str(ip))
ips = ips[1:-1]
# subnet = ['10.69.250.100', '10.69.250.2', '10.69.250.3']

def discover(ip):
    try:
        # print(ip)
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community, mpModel=0),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            # print(errorIndication)
            pass

        elif errorStatus:
            # print('%s at %s' % (errorStatus.prettyPrint(),
            #                     errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            pass

        else:
            for varBind in varBinds:
                output = str(varBind)
                # print(f"{ip} {' = '.join([x.prettyPrint() for x in varBind])}")
                print(f"{ip} {output.split()[2]}")
        # time.sleep(5)
    except:
        pass



try:
    for ip in ips:
        thread = threading.Thread(target=discover, args=(ip,))
        thread.start()
except Exception as e:
    print(e)