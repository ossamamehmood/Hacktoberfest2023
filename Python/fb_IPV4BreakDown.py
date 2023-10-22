#required pip install netaddr and ipaddress 

from netaddr import * 
import ipaddress

def ValidateIPv4(ip):
    #validate ip is not empty
    if ip == "":
        return False
    
    if len(ip) > 18:
        return False
    
    if len(ip)< 7:
        return False

    # split the ip in 2 parts
    splitIP = ip.split('/')
    ipnum = splitIP[0]
    prefix = splitIP[1]
    # check prefix
    if int(prefix) > 32 or int(prefix) < 0:
        return False
    # split the ip in 4 parts
    splitIP = ipnum.split('.')
    # check if the ip is valid
    if len(splitIP) != 4:
        return False
    for i in splitIP:
        if int(i) > 255 or int(i) < 0:
            return False

    # return the ip adn prefix
    return True


ip = input(
    "Please enter an IP address with a subnet prefix for example 192.168.2.155/25: ")

while ValidateIPv4(ip) == False:
    print("The correct format is [0-255].[0-255].[0-255].[0-255] / [8-31]")
    ip = input(
        "Please enter an IP address with a subnet prefix for example 192.168.2.155/25: ")

    continue


address = ipaddress.ip_network(ip, strict=False)

ip_adress = ip.split('/')[0]
bin_ip_adrress = IPAddress(ip_adress).bits()
# print the ip address and binary representation
print(f"IP address: \t{ip_adress}\t\t{bin_ip_adrress}")



#Netmask and bin mask
netmask = address.netmask
binmask = IPAddress(str(netmask)).bits()
print(f"Netmask: \t{netmask} \t\t{binmask}")

#wildcard mask and bin mask
wildcard = address.hostmask
binwild = IPAddress(str(wildcard)).bits()
print(f"Wildcard mask: \t{wildcard} \t\t{binwild}")

print("----------------------------------------------------------------------------")

#network address and bin address
ip =ipaddress.IPv4Network(ip, strict=False)
network = ip.network_address
binnetwork = IPAddress(str(network)).bits()
print(f"Network address: {network} \t\t{binnetwork}")

#broadcast address and bin address
broadcast = ip.broadcast_address
binbroadcast = IPAddress(str(broadcast)).bits()
print(f"Broadcast address: {broadcast} \t{binbroadcast}")

#Hostmin and bin hostmin
ip =ipaddress.IPv4Network(ip, strict=False)
hostlist = list(ip.hosts())
hostmin = hostlist[0]
binhostmin = IPAddress(str(hostmin)).bits()
print(f"Hostmin: \t{hostmin} \t\t{binhostmin}")

#Hostmax and bin hostmax
hostmax = hostlist[-1]
binhostmax = IPAddress(str(hostmax)).bits()
print(f"Hostmax: \t{hostmax} \t\t{binhostmax}")

#host/net
hostnet = ip.num_addresses - 2
print(f"Host/Net: \t{hostnet}")
