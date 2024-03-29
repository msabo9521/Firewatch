import ipaddress

addresses = '10.69.250.0/24'
community = 'sabonetro'
subnet = ipaddress.ip_network(addresses)

def test():
    ips = []
    for ip in subnet:
        ips.append(str(ip))

    ips = ips[1:-1]
    for x in ips:
        print(x)
