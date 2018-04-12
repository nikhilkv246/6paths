#!/usr/bin/env python

from scapy.all import *
from datetime import datetime
import time
import datetime
import sys

interface = 'eth0'
filter_bpf = 'udp and port 53'
query_count = 0

def select_DNS(pkt):
	pkt_time = pkt.sprintf('%sent.time%')
	global query_count

	try:
		if DNSQR in pkt and pkt.dport == 53:
			query_count += 1
			print '[**] Detected DNS Query Message at: ' + pkt_time
			print "Packet Count: ", query_count
			

	except:
		pass

sniff(iface=interface, filter=filter_bpf, store=0,  prn=select_DNS)
