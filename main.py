"""
Subnetting Tool

This program is designed to assist network engineers and administrators in performing subnetting calculations efficiently. Subnetting is a process used to divide a single, large network into smaller, manageable sub-networks, allowing for efficient use of IP addresses and better network organization.

The Subnetting Tool provides the following functionality:

1. Subnet Calculation: Given an IP address and subnet mask in dotted decimal format (e.g., 192.168.1.0/24) or CIDR notation (e.g., 192.168.1.0/255.255.255.0), the tool calculates network address, broadcast address, range of usable IP addresses, and subnet mask in CIDR notation for each subnet.

2. Supernetting: Users can perform supernetting to combine multiple smaller subnets into a larger supernet, simplifying routing and reducing routing table size.

3. Merging: The tool allows users to merge contiguous subnets into larger subnets, optimizing IP address usage and network efficiency.

4. Dividing: Users can divide larger subnets into smaller subnets, providing flexibility in network design and accommodating changing network requirements.

This tool simplifies the process of subnetting, supernetting, merging, and dividing by automating calculations, supporting both dotted decimal and CIDR notation, and providing clear visualizations, saving time and effort for network professionals.

Author: [Caroline Ek]
Date: [March 31, 2024]
"""

from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor
    
    @abstractmethod
    def handle_request(self, choice):
        pass
    
class SubnetCalculationHandler(Handler):
    def handle_request(self, choice):
        if choice == '1':
            print("=======================")
            print("\nHandling Subnet Calculation")
            print("=======================")
            
            ip = input("What is the IP address? ")
            mask = input("What is the subnet mask? ")
            
            subnetCalculator(ip, mask)
            
        elif self.successor:
            self.successor.handle_request(choice)

class SupernettingHandler(Handler):
    def handle_request(self, choice):
        if choice == '2':
            print("=======================")
            print("\nHandling Supernetting")
            print("=======================")
        elif self.successor:
            self.successor.handle_request(choice)

class MergingHandler(Handler):
    def handle_request(self, choice):
        if choice == '3':
            print("=======================")
            print("\nHandling Merging")
            print("=======================")
        elif self.successor:
            self.successor.handle_request(choice)

class DividingHandler(Handler):
    def handle_request(self, choice):
        if choice == '4':
            print("=======================")
            print("\nHandling Dividing")
            print("=======================")
        elif self.successor:
            self.successor.handle_request(choice)
            

def subnetCalculator(ipAddr, subnetMask):
    
    
def ip_to_binary(ip):
    return '.'.join([bin(int(x)+256)[3:] for x in ip_address.split('.')])
    

# Setting up the chain of responsibility
subnet_handler = SubnetCalculationHandler()
supernet_handler = SupernettingHandler(subnet_handler)
merging_handler = MergingHandler(supernet_handler)
dividing_handler = DividingHandler(merging_handler)

# Usage
print("=========== Subnetting Tool ================")
print("1. Subnet Calculation (Both dotted decimal and CIDR notation are available.)")
print("2. Supernetting")
print("3. Merging")
print("4. Dividing\n")
choice = input("What would you like to do? ")

dividing_handler.handle_request(choice)



