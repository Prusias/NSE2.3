def get_ipv4_from_host(host):
    if 'ipv4' in host['addresses']:
        return host['addresses']['ipv4'] 
    else:
        return 'unknown'

def get_mac_from_host(host):
    if 'mac' in host['addresses']:
        return host['addresses']['mac'] 
    else:
        return 'unknown'

def get_hostnames_from_host(host):
    hostnames = []

    for hostname in host['hostnames']:
        hostnames.append(hostname['name'])

    return hostnames

def get_os_from_host(host, min_accuracy = 95):
    osmatches = []
    
    for osmatch in host['osmatch']:
        if (int(osmatch['accuracy']) > min_accuracy):
            osmatches.append(osmatch)

    return osmatches   

def get_services_from_host(nm, host):
    services = []

    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        for port in lport:
            services.append({'protocol': proto, 'port': port, 'name': nm[host][proto][port]['name']})
    
    return services

def get_ports_from_host(host):
    ports = []

    try:
        for port in host['tcp']:
            ports.append(port)
    except:
        pass

    return ports   
    