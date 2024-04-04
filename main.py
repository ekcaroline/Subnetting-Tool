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
#Notes:
#Try using socket for converting the IP addresses to binary.

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
            print("Handling Subnet Calculation")
            print("=======================")
            
            while True:
                ip = input("What is the IP address? ")
                splitIP = ip.split(".")
                
                if len(splitIP) == 4:  # Check if IP has exactly 4 parts
                    valid = True
                    for part in splitIP:
                        if not 1 <= len(part) <= 3 or not 0 <= int(part) <=255:
                            valid = False
                            break
                    if valid:
                        break
                print("Invalid IP. Each part must be 1 to 3 characters in length or range from 0-255. Try again.")
                
            while True:
                method = input("Would you like to use (1) CIDR or (2) Classful Notation? \n")
                
                if method == '1':
                    mask = input("What is the subnet mask? (No need to put in the slash.) \n/")
                    subnetCIDR(ip, mask)
                    break
                elif method == '2':
                    mask = input("What is the subnet mask? (Dotted decimal notation.)")
                    subnetClassful(ip, mask)
                    break
                else:
                    print("Invalid choice. Try again.")
                
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
        while True:
            if choice == '4':
                print("=======================")
                print("\nHandling Dividing")
                print("=======================")
                break
            elif choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Try again.")
                choice = input("Enter your choice (1-4): ")
            elif self.successor:
                self.successor.handle_request(choice)
                break
            

def subnetCIDR(ipAddr, subnetMask):
    
    binIP = IPtoBinary(ipAddr)
    print(binIP, "is the IP address in binary. It has been successfully converted. \nNow I will perform the calculation.")

def subnetClassful(ipAddr, subnetMask): #work on
    return 0
    
def IPtoBinary(ip):
    return '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])

def binaryToIP(binary):
    octets = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return '.'.join([str(int(octet, 2)) for octet in octets])

# Setting up the chain of responsibility
subnet_handler = SubnetCalculationHandler()
supernet_handler = SupernettingHandler(subnet_handler)
merging_handler = MergingHandler(supernet_handler)
dividing_handler = DividingHandler(merging_handler)

def mainMenu():
    # Usage
    print("=========== Subnetting Tool ================")
    print("1. Subnet Calculation (Both dotted decimal and CIDR notation are available.)")
    print("2. Supernetting")
    print("3. Merging")
    print("4. Dividing\n")
    choice = input("What would you like to do? ")

    dividing_handler.handle_request(choice)
    
mainMenu()



