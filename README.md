# MAC Address Changer

This Tool is used to change MAC Address of Linux Machines.

# Information
This tool is for educational purpose only, usage of macchanger for attacking targets without prior mutual consent is illegal. Developer assume no liability and is not responsible for any misuse or damage cause by this program.

# Download

	git clone https://github.com/inavedanjum/macchanger.git
	cd macchanger
	chmod +x macchanger.py

# Usage
	
	python macchanger.py -i <interface> -m <new_mac>
	                        or 
	python macchanger.py --interface <interface> --mac <new_mac>
	
	example:
	python macchanger.py -i eth0 --mac 00:11:11:11:11:23


