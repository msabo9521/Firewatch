from pysnmp.hlapi import *


def snmp_get(ip, community, oid):
    try:
        # print(ip)
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community, mpModel=0),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
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
                if oid == '1.3.6.1.2.1.1.2.0':
                    output = '.'.join(str(varBind).split('enterprises')[1].split('.')[1:])
                else:
                    print(varBind)
                    output = ' '.join(str(varBind).split()[2:])
                # print(f"{ip} {' = '.join([x.prettyPrint() for x in varBind])}")
                return(output)
        # time.sleep(5)
    except:
        pass

oid = '1.3.6.1.2.1.47.1.1.1.1.11.1'
# print(snmp_get('10.69.110.1', 'sabonetro', oid))
print(snmp_get('10.69.110.2', 'sabonetro', oid))
# print(snmp_get('10.69.250.4', 'sabonetro', oid))


