"""
    [DESCRIPTION]: This program allows us to collect some information
                   so we can split up the networks.
    
                              (SUBNET TABLE):
                    ------------------------------------
    Subnets:         1   2   4   8   16  32  64  128 256
    Hosts:          256 128  64  32  16  8   4   2   1
                    ------------------------------------
    Subnet Mask:    /24 /25 /26 /27 /28 /29 /30 /31 /32
"""
__title__ = "Subnetting"
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"

import re

class Subnetting:
    """
    Name        :   Subnetting
    Purpose     :   This class will contain methods that will help with
                    subnetting networks.
    """

    _two_hundred_fifty_six = 256
    _thirty_two = 32

    def __init__(self, ipaddress, subnet_mask="255.255.255.0"):
        self.ipaddress = ipaddress
        self.subnet_mask = subnet_mask

    # Determines the ip class.
    def determine_ip_class(self):
        expression = re.search("(\d{1,3})", self.ipaddress)
        if (expression):
            firstOctet = int(expression.group(0))
            if (1 <= firstOctet <= 127):
                return 'A'
            elif (128 <= firstOctet <= 191):
                return 'B'
            elif (192 <= firstOctet <= 223):
                return 'C'
            elif (224 <= firstOctet <= 239):
                return 'D'
            elif (240 <= firstOctet <= 255):
                return 'E'
    
    # Determines the number of mask bits.
    def determine_mask_bits(self):
        subnet_expression = re.search("(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})", self.subnet_mask)
        if (subnet_expression):
            
            octet_one_sub = bin(int(subnet_expression.group(1)))
            octet_two_sub = bin(int(subnet_expression.group(2)))
            octet_three_sub = bin(int(subnet_expression.group(3)))
            octet_four_sub = bin(int(subnet_expression.group(4)))

            one = octet_one_sub
            two = octet_two_sub
            three = octet_three_sub
            four = octet_four_sub
            
            count_octet_one = 0
            for nums in range(2, len(one)):
                if (one[nums] == '1'):
                    count_octet_one = count_octet_one + 1

            count_octet_two = 0
            for nums in range(2, len(two)):
                if (two[nums] == '1'):
                    count_octet_two = count_octet_two + 1

            count_octet_three = 0
            for nums in range(2, len(three)):
                if (three[nums] == '1'):
                    count_octet_three = count_octet_three + 1
            
            count_octet_four = 0
            for nums in range(2, len(four)):
                if (four[nums] == '1'):
                    count_octet_four = count_octet_four + 1

            total_count = count_octet_one + count_octet_two + count_octet_three + count_octet_four
            return total_count


    # Determines the quantity of subnet bits.
    def determine_subnet_bits(self, mask_bits):
        subnet_expression = re.search("(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})", self.subnet_mask)
        if (subnet_expression):
            ip = self.determine_ip_class()
            if (ip == 'A'):
                group_one_sub = bin(int(subnet_expression.group(3)))
                length_of_sub = len(group_one_sub)
            elif (ip == 'B'):
                group_one_sub = bin(int(subnet_expression.group(3)))
                length_of_sub = len(group_one_sub)
            elif (ip == 'C'):
                group_one_sub = bin(int(subnet_expression.group(4)))
                length_of_sub = len(group_one_sub)

            count_last_octet = 0
            for nums in range(0, length_of_sub):
                if (group_one_sub[nums] == '1'):
                    count_last_octet = count_last_octet + 1
            return count_last_octet

    @staticmethod
    def determine_maximum_subnets(subnet_bits):
        if (subnet_bits is not None):
            maximum_subnets = 2 ** subnet_bits
            return maximum_subnets
        else:
            return -1

    # This calculate the network address.
    def calculate_network_address(self):
        expression = re.search("(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})", self.ipaddress)
        subnet_expression = re.search("(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})", self.subnet_mask)
        if (expression and subnet_expression):
            octet_one = int(expression.group(1))
            octet_two = int(expression.group(2))
            octet_three = int(expression.group(3))
            octet_four = int(expression.group(4))

            octet_one_sub = int(subnet_expression.group(1))
            octet_two_sub = int(subnet_expression.group(2))
            octet_three_sub = int(subnet_expression.group(3))
            octet_four_sub = int(subnet_expression.group(4))

            one = octet_one & octet_one_sub
            two = octet_two & octet_two_sub
            three = octet_three & octet_three_sub
            four = octet_four & octet_four_sub

            network_address = str(one) + "." + str(two) + "." + str(three) + "." + str(four)
            return network_address

    def calculate_maximum_hosts_in_subnet(self, mask_bits):
        if (mask_bits is not None):
            number_of_hosts = (2 ** (32 - mask_bits)) - 2
            return number_of_hosts
        else:
            return -1
    
    
if __name__ == "__main__":

    # [IMPORTANT]: Be sure you adjust both ip and subnet mask to match your result.
    #_ipaddress = "10.0.0.1"
    #_subnet_mask = "255.0.0.0"
    #_ipaddress = "128.65.5.2"
    #_subnet_mask = "255.255.0.0"
    _ipaddress = "192.168.100.0"
    _subnet_mask = "255.255.255.128"
    sub = Subnetting(_ipaddress, _subnet_mask)

    whatClassIsIp = sub.determine_ip_class()
    if (whatClassIsIp == 'A'):
        network_address_a = sub.calculate_network_address()
        mask_bits_a = sub.determine_mask_bits()
        subnet_bits_a = sub.determine_subnet_bits(mask_bits_a)
        maximum_subnets_a = sub.determine_maximum_subnets(subnet_bits_a)
        maximum_host_number_a = sub.calculate_maximum_hosts_in_subnet(mask_bits_a)

        print("Class: ", whatClassIsIp)
        print("Network address:", network_address_a)
        print("Mask bits:", mask_bits_a)
        print("Subnet bits:", subnet_bits_a)
        print("Maximum subnets:", maximum_subnets_a)
        print("Maximum amount of hosts:", maximum_host_number_a)
    elif (whatClassIsIp == 'B'):
        network_address_b = sub.calculate_network_address()
        mask_bits_b = sub.determine_mask_bits()
        subnet_bits_b = sub.determine_subnet_bits(mask_bits_b)
        maximum_subnets_b = sub.determine_maximum_subnets(subnet_bits_b)
        maximum_host_number_b = sub.calculate_maximum_hosts_in_subnet(mask_bits_b)

        print("Class: ", whatClassIsIp)
        print("Network address:", network_address_b)
        print("Mask bits:", mask_bits_b)
        print("Subnet bits:", subnet_bits_b)
        print("Maximum subnets:", maximum_subnets_b)
        print("Maximum amount of hosts:", maximum_host_number_b)
    elif (whatClassIsIp == 'C'):
        network_address_c = sub.calculate_network_address()
        mask_bits_c = sub.determine_mask_bits()
        subnet_bits_c = sub.determine_subnet_bits(mask_bits_c)
        maximum_subnets_c = sub.determine_maximum_subnets(subnet_bits_c)
        maximum_host_number_c = sub.calculate_maximum_hosts_in_subnet(mask_bits_c)

        print("Class: ", whatClassIsIp)
        print("Network address:", network_address_c)
        print("Mask bits:", mask_bits_c)
        print("Subnet bits:", subnet_bits_c)
        print("Maximum subnets:", maximum_subnets_c)
        print("Maximum amount of hosts:", maximum_host_number_c)
    elif (whatClassIsIp == 'D'):
        print("Multicast !")
    elif (whatClassIsIp == 'E'):
        print("Reserved !")
    else:
        print("Not a proper address !")
    
    