#!/usr/bin/env python3
from ncclient import manager
from netaddr import IPAddress
from netmiko import ConnectHandler
import unittest
import ipaddress

#Adding this to test the webhook again


def main():
    router = {
        "device_type": "cisco_ios",
		"ip": "198.51.100.12",
		"username": "lab",
		"password": "lab123",
		"secret": "lab123"
    }

    with ConnectHandler(**router) as net_connect:
        output = net_connect.send_command("ping 10.1.5.1 source 10.1.2.1")
    print(output.split("\n")[3])


if __name__ == "__main__":
    main()
