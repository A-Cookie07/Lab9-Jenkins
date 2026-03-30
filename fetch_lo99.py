#!/usr/bin/env python3
from ncclient import manager
from netaddr import IPAddress
from netmiko import ConnectHandler
import unittest
import ipaddress


FETCH_INFO = '''
    		<filter>
    		<config-format-text-block>
    		<text-filter-spec> %s </text-filter-spec>
    		</config-format-text-block>
    		</filter>
    		'''

PING_COMMAND = '''
    		<filter>
    		<config-format-text-block>
    		do ping 198.51.100.2
    		</config-format-text-block>
    		</filter>
    		'''

def fetch_99():
    connection = manager.connect(host='198.51.100.13',
                                     port=22,
                                     username='lab',
                                     password='lab123',
                                     hostkey_verify=False,
                                     device_params={'name': 'iosxr'},
                                     allow_agent=False,
                                     look_for_keys=False)

    
    fetch_lo_info = FETCH_INFO % ('int Loopback99')
    output2 = connection.get_config('running', fetch_lo_info)
    split2 = str(output2).split()
    lo_ip_mask = split2[9] + '/' + str(IPAddress(split2[10]).netmask_bits())
    #print(lo_ip_mask)
    return(str(lo_ip_mask))

def fetch_areas():
    #This tests if only one area is configured on a router
    connection = manager.connect(host='198.51.100.11',
                                     port=22,
                                     username='lab',
                                     password='lab123',
                                     hostkey_verify=False,
                                     device_params={'name': 'iosxr'},
                                     allow_agent=False,
                                     look_for_keys=False)

    #The way we test for only one area is getting every line where area is mentioned in the conf
    #(Should only be ospf area on interface or in ospf config)
    fetch_ospf_info = FETCH_INFO % ('| i area')
    output3 = connection.get_config('running', fetch_ospf_info)

    #Strip off the xml <data-blocks>
    split3 = str(output3).split("data-block>\n")
    split3 = split3[1]
    split3 = split3.split('</cli-config')
    split3 = split3[0]

    #Then divide up the configs by line, and store the value after area (i.e "area 0", "area 1")
    #in a dictionary, then make sure the length is only 1.  This means there is only one area configured
    #as if there were more there would be more entries in the dictionary.
    split3 = split3.split('\n')
    area = {}
    for i in split3:
        area[i.split('area ')[1].strip()] = "included"
    return(len(area))

def ping_if():
    router = {
        "device_type": "cisco_ios",
		"ip": "198.51.100.12",
		"username": "lab",
		"password": "lab123",
		"secret": "lab123"
    }

    with ConnectHandler(**router) as net_connect:
        output = net_connect.send_command("ping 10.1.5.1 source 10.1.2.1")
    return(output.split("\n")[3])

    

class TestRemoteConfig(unittest.TestCase):
    def test_unittest(self):
        """Test That Unit Tests Work"""
        self.assertEqual(2+2, 4)

    def test_ping_interface(self):
        """Testing that router can ping"""
        self.assertEqual(ping_if(),'!!!!!')

    def test_loopback99(self):
        """Test That Loopback is correct"""
        self.assertEqual(fetch_99(),'10.1.3.1/24')

    def test_1_area(self):
        """Testing that the Area Value that is used for the table for R1 is 0"""
        self.assertEqual(fetch_areas(),1)

    

if __name__ == "__main__":
    unittest.main(verbosity=2)
