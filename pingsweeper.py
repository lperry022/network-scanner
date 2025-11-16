# =========Import Modules=========
import sys
# sys is used to interact with the command line
from scapy.all import ICMP, IP, sr1
# scapy is used for packet manipulation and sending/receiving packets
from netaddr import IPNetwork
# netaddr is used for handling IP addresses and networks
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
# hide scapy warnings for cleaner output

# =========Ping sweep function=========


def ping_sweep(network, netmask):
    live_hosts = []  # empty list to store live hosts for every host that is online
    total_hosts = 0  # used to count total hosts scanned
    scanned_hosts = 0  # used to count total hosts that are online

# the function ping_sweep receives a network and netmask as input parameters.
    ip_network = IPNetwork(network + '/' + netmask)
    for host in ip_network.iter_hosts():
        total_hosts += 1
# this is the ip address object that will return the actual ip addresses on the network
# iter_hosts() method generates all usable host IP addresses in the network
    for host in ip_network.iter_hosts():
        # this loop will iterate through each host in the network
        scanned_hosts += 1
        print(f"Scanning host: {scanned_hosts}/{total_hosts}", end="\r")
        # keeps count of all scanned ip addresses and prints progress to the console
        response = sr1(IP(dst=str(host)) / ICMP(), timeout=1, verbose=0)
        # sr1() sends a single packet and waits for a response
        if response is not None:
            live_hosts.append(str(host))
            print(f"Host {host} is online.")
        # if a response is received, the host is considered online and added to the live_hosts list
    return live_hosts


    # =========Main function=========
if __name__ == "__main__":
    network = sys.argv[1]  # first command line argument is the network address
    netmask = sys.argv[2]  # second command line argument is the netmask
    live_hosts = ping_sweep(network, netmask)
    print("Completed scan.")
    print(f"Live hosts: {live_hosts}")
