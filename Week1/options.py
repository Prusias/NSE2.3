class ScanOptions:
    def __init__(self):
        self.scan_ip = True
        self.scan_mac = False
        self.scan_hostname = False
        self.scan_os = False
        self.scan_services = False
        self.scan_ports = False
        # self.ports_to_scan = ''
        self.hosts_to_scan = ''

    def fill_from_arguments(self, arguments):
        if ("-mac" in arguments):
            self.scan_mac = True
        if ("-hostname" in arguments):
            self.scan_hostname = True
        if ("-os" in arguments):
            self.scan_os = True
        if ("-services" in arguments):
            self.scan_services = True
        if ("-ports" in arguments):
            self.scan_ports = True
            # arg_index = arguments.index('-ports')
            # self.ports_to_scan = arguments[arg_index + 1]
        if ("-h" in arguments):
            arg_index = arguments.index('-h')
            self.hosts_to_scan = arguments[arg_index + 1]
        else:
            self.hosts_to_scan = '127.0.0.1'
            


    def get_arguments(self):
        arguments = ''
        if (self.scan_os == False and self.scan_ports == False and self.scan_services == False):
            arguments += '-sn'
        else:
            arguments += '-sS'
        if (self.scan_os == True):
            arguments += ' -O'
        if (self.scan_hostname == True):
            arguments += ' -R'
        if (self.scan_services == True):
            arguments += ' -sV'
        if (self.scan_ports == True):
            arguments += ' -r'
        return arguments
        