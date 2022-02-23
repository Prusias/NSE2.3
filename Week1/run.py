from options import ScanOptions
from output import *
import nmap
from datetime import datetime

def run(options: ScanOptions):
    print('Scanning: %s' % options.hosts_to_scan)
    print('Arguments used: %s' % options.get_arguments())

    nm = nmap.PortScanner()
    nm.scan(hosts = options.hosts_to_scan, arguments = options.get_arguments())

    timestamp = str(datetime.now())
    filename = 'scan_result_%s.txt' % timestamp

    print_to_file(nm, options, filename, timestamp)

    print('Output scan results to: %s' % filename)