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
            
            # Ask for IP address and check if it is valid 
            while True:
                ip = input("What is the IP address? ")
                splitIP = ip.split(".")
                
                if len(splitIP) == 4:  
                    valid = True
                    for part in splitIP:
                        if not 1 <= len(part) <= 3 or not 0 <= int(part) <=255:
                            valid = False
                            break
                    if valid:
                        break
                print("Invalid IP. Each part must be 1 to 3 characters in length or range from 0-255. Try again.")
            
            # Notations and subnet mask !!FIX
            method = input("Would you like to use (1) CIDR or (2) Classful Notation? ")
            while True:
                print("\n** Note **: \nIf using CIDR, please format using slash. '/XX'.")
                print("If using Classful, please format in dotted decimal notation. Thank you!\n\n")
                mask = input("What is the subnet mask? Need to convert subnet? Press 'U'. ")
                
                if method == '1':
                    # Check if the first character is '/'
                    if mask and mask[0] != '/':
                        print("Invalid subnet mask format. Please enter the subnet mask in dotted decimal notation or CIDR notation.")
                        print("========================================")
                        continue
                    
                    cidrMask = mask[1:]
                    if int(cidrMask) < 0 or int(cidrMask) > 32:
                        print("Invalid subnet mask. Please enter a number between 0 and 32.")
                    elif mask.lower() == 'u':
                        convertSubnet()
                    else:
                        subnetCIDR(ip, cidrMask )
                        break
                elif method == '2':
                    classfulSubnet = ['255.0.0.0', '255.255.0.0', '255.255.255.0']
                    if mask not in classfulSubnet:
                        print("Invalid subnet mask. Please try again.")
                        print("========================================")
                    elif mask.lower() == 'u':
                        convertSubnet()
                    else:
                        subnetClassful(ip, mask)
                        break
                else:
                    print("Invalid choice. Please enter either '1' or '2'.")


        elif self.successor:
            self.successor.handle_request(choice)

class SupernettingHandler(Handler):
    def handle_request(self, choice):
        if choice == '2':
            print("=======================")
            print("Handling Supernetting")
            print("=======================")
        elif self.successor:
            self.successor.handle_request(choice)

class MergingHandler(Handler):
    def handle_request(self, choice):
        if choice == '3':
            print("=======================")
            print("Handling Merging")
            print("=======================")
        elif self.successor:
            self.successor.handle_request(choice)

class DividingHandler(Handler):
    def handle_request(self, choice):
        if choice == '4':
            print("=======================")
            print("Handling Dividing")
            print("=======================")
        elif self.successor:
            self.successor.handle_request(choice)

            
class OtherHandler(Handler): #work on
    def handle_request(self, choice):
        while True:
            if choice == '5':
                print("=======================")
                print("Handling Other")
                print("=======================")
                
                print("\nOther options:")
                print("1. Convert subnet mask to '/'")
                print("2. Convert IP address")
                print("3. Convert wildcard mask")
                otherChoice = input("\nWhat would you like to do? ")
                break
            elif choice not in ['1', '2', '3', '4', '5']:
                print("Invalid choice. Try again.")
                choice = input("Enter your choice (1-5): ")
            elif self.successor:
                self.successor.handle_request(choice)
                break
        
            

def subnetCIDR(ipAddr, subnetMask):
    lengthIP = 32
    binIP = IPtoBinary(ipAddr)

    print(binIP, "is the IP address in binary. It has been successfully converted. \n")
    print("Calculating...")

    #Calculate the network address 
    ipWithoutDecimal = binIP.replace(".", "")
    partNetAddr = ipWithoutDecimal[:int(subnetMask)]
    bitsToZeroOutN = lengthIP - int(subnetMask)
    fullNetAddr = partNetAddr + "0" * bitsToZeroOutN
    networkAddr = binaryToIP(fullNetAddr)
    print("Network Address:", networkAddr)

    #Calculte the host address 
    partHostAddr = ipWithoutDecimal[int(subnetMask):]
    bitsToZeroOutH = lengthIP - int(subnetMask)
    fullHostAddr = "0" * bitsToZeroOutH + partHostAddr
    hostAddr = binaryToIP(fullHostAddr)
    print("Host Address:", hostAddr)

def subnetClassful(ipAddr, subnetMask): #work on
    classA = range(1, 126)
    classB = range(128, 191)
    classC = range(192, 223)

    return 0
    
def IPtoBinary(ip):
    return '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])

def binaryToIP(binary):
    octets = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return '.'.join([str(int(octet, 2)) for octet in octets])

def convertSubnet(): #work on
    typeChoice = input("Is the subnet mask in (1) Dotted decimal or (2) '/' ? ")
    if int(typeChoice) == 1:
        return
    elif int(typeChoice) == 2:
        return

# Setting up the chain of responsibility
subnet_handler = SubnetCalculationHandler()
supernet_handler = SupernettingHandler(subnet_handler)
merging_handler = MergingHandler(supernet_handler)
dividing_handler = DividingHandler(merging_handler)
other_handler = OtherHandler(dividing_handler)

def mainMenu():
    # Usage
    print("=========== Subnetting Tool ================")
    print("1. Subnet Calculation (Both dotted decimal and CIDR notation are available.)")
    print("2. Supernetting")
    print("3. Merging")
    print("4. Dividing")
    print("5. Other\n")
    choice = input("What would you like to do? ")

    other_handler.handle_request(choice)
    
mainMenu()







