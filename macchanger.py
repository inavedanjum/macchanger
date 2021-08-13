#!/usr/bin/env python3

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change mac address")
    parser.add_option("-m", "--mac", dest = "new_mac", help = " Enter New Mac Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please Specify a new MAC address, use --help for more info.")
    return options
        

def mac_changer(interface, new_mac):
    
    print("[+] Changing MAC address for " + interface +" to New MAC " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface,"hw","ether",new_mac ])
    subprocess.call(["ifconfig", interface, "up" ])

def get_current_mac(interface):
    
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_add_srh_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w\:\w\w", ifconfig_result)
    if mac_add_srh_res:
        return mac_add_srh_res.group(0)
    else:
        print("[-] Module doesn't contain MAC address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
mac_changer(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC Address successfully changed to "+ current_mac )
else:
    print("[-] Error MAC address not changed, use --help for more info ")
    