from options import ScanOptions
from getters import *
import sys

def print_to_console(nm, host, options: ScanOptions):
    print('host:')
    if options.scan_ip:
        print('\tipv4: ' + get_ipv4_from_host(nm[host]))
    if options.scan_mac:
        print('\tmac: ' + get_mac_from_host(nm[host]))

    if options.scan_hostname:
        hostnames = get_hostnames_from_host(nm[host])
        print('\thostnames:')

        if len(hostnames > 0):
            for name in hostnames:
                print('\t\t' + name)
        else:
            print('\t\tnone found')

    if options.scan_os:
        os_list = get_os_from_host(nm[host])
        print('\tos:')
        if len(os_list) > 0:
            for os in os_list:
                print('\t\tname: %s' % os['name'])
                print('\t\t\taccuracy: %s' % os['accuracy'])
        else:
            print('\t\tnone found')

    if options.scan_services:
        services = get_services_from_host(nm, host)
        print('\tservices:')

        if len(services) > 0:
            for service in services:
                print('\t\tname: %s' % service['name'])
                print('\t\t\tprotocol: %s' % service['protocol'])
                print('\t\t\tport: %s' % service['port'])
        else:
            print('\t\tnone found')

    if options.scan_ports:
        ports = get_ports_from_host(nm[host])
        print('\tport:')
        if len(ports) > 0:
            for port in ports:
                print('\t\t %s' % port)
        else:
            print('\t\tnone found')

def print_to_file(nm, options: ScanOptions, filename, timestamp):
    with open(filename, 'w') as file:
        original_stdout = sys.stdout

        sys.stdout = file

        print('Scan results from nmap')
        print('Run at %s' % timestamp)
        print('Arguments %s' % options.get_arguments())
        print('Hosts %s' % options.hosts_to_scan)
        print()

        for host in nm.all_hosts():
            print_to_console(nm, host, options)
            print()

        sys.stdout = original_stdout