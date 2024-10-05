from scapy.all import *
import socket

def print_summary(pkt):
    if 'IP' in pkt:
        ip_src=pkt['IP'].src
        ip_dst=pkt['IP'].dst
    if 'TCP' in pkt:
        tcp_sport=pkt['TCP'].sport
        tcp_dport=pkt['TCP'].dport

    try:
        print(" IP src " + str(ip_src) + " TCP sport " + str(tcp_sport))
        print(" IP dst " + str(ip_dst) + " TCP dport " + str(tcp_dport))
    except:
        pass

    # you can filter with something like that
    if ( ( pkt['IP'].src == "192.168.0.1") or ( pkt['IP'].dst == "192.168.0.1") ):
        print("!")

sniff(filter="ip",prn=print_summary)
