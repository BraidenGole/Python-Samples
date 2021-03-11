"""
    [DESCRIPTION]: Python 3

    This is a limited converter !

"""
__title__ = "Limited converter"
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"
__date__ = "2021-03-11"

class Converter:
    """
    Name        :   Converter
    Purpose     :   This class will hold methods that will convert
                    one computational unit to another.
    """

    # Converts decimal to binary.
    @staticmethod
    def dec_to_bin(decimal):
        conversion = []
        while decimal > 0:
            conversion.append(decimal % 2)
            decimal = decimal // 2
        return conversion

    # Binary to decimal.
    @staticmethod
    def bin_to_dec(binary_number):
        conversion = 0
        length_of_number = len(binary_number)
        decrement_length = length_of_number
        for digit in range(0, length_of_number):
            decrement_length = decrement_length - 1
            conversion += int(binary_number[digit]) * 2 ** decrement_length
        return conversion

    # A quick easy way to convert by a fixed map.
    @staticmethod
    def hex_to_bin(hex_code):
        if hex_code == 0:
            return "0000"
        elif hex_code == 1:
            return "0001"
        elif hex_code == 2:
            return "0010"
        elif hex_code == 3:
            return "0011"
        elif hex_code == 4:
            return "0100"
        elif hex_code == 5:
            return "0101"
        elif hex_code == 6:
            return "0110"
        elif hex_code == 7:
            return "0111"
        elif hex_code == 8:
            return "1000"
        elif hex_code == 9:
            return "1001"
        elif hex_code == 'A':
            return "1010"
        elif hex_code == 'B':
            return "1011"
        elif hex_code == 'C':
            return "1100"
        elif hex_code == 'D':
            return "1101"
        elif hex_code == 'E':
            return "1110"
        elif hex_code == 'F':
            return "1111"

    # A quick and easy way to convert by fixed map.
    @staticmethod
    def bin_to_hex(hex_code):
        if hex_code == "0000":
            return 0
        elif hex_code == "0001":
            return 1
        elif hex_code == "0010":
            return 2
        elif hex_code == "0011":
            return 3
        elif hex_code == "0100":
            return 4
        elif hex_code == "0101":
            return 5
        elif hex_code == "0110":
            return 6
        elif hex_code == "0111":
            return 7
        elif hex_code == "1000":
            return 8
        elif hex_code == "1001":
            return 9
        elif hex_code == "1010":
            return 'A'
        elif hex_code == "1011":
            return 'B'
        elif hex_code == "1100":
            return 'C'
        elif hex_code == "1101":
            return 'D'
        elif hex_code == "1110":
            return 'E'
        elif hex_code == "1111":
            return 'F'

    # Converts from octal to decimal.
    def oct_to_dec(self, octal_code):
        conversion = 0
        length_of_number = len(octal_code)
        decrement_length = length_of_number
        for digit in range(0, length_of_number):
            decrement_length = decrement_length - 1
            conversion += int(octal_code[digit]) * 8 ** decrement_length
        return conversion

    # Converts from decimal to octal.
    def dec_to_oct(self, decimal):
        length_of_decimal = len(decimal) -3
        dec_copy = int(decimal)
        iter = 0
        store = [0] * length_of_decimal
        while dec_copy != 0:
            store.insert(iter, dec_copy % 8)
            dec_copy = dec_copy // 8
            iter = iter + 1
        return store

    # Give us readable representations of the answers below.
    @staticmethod
    def print_forwards(answer_to_reverse):
        for num in reversed(answer_to_reverse):
            print(num, end="")


if __name__ == "__main__":

    convert = Converter()

    # We must print the answer reverse to properly read the binary number.
    answer = convert.dec_to_bin(8)
    convert.print_forwards(answer)

    print()

    answer2 = convert.bin_to_dec("1000")
    print(answer2)

    answer3 = convert.hex_to_bin('A')
    print(answer3)

    answer4 = convert.bin_to_hex("0111")
    print(answer4)

    answer5 = convert.oct_to_dec("437")
    print(answer5)

    # We must use the function print_forwards to read the decimal number properly.
    answer6 = convert.dec_to_oct("169")
    convert.print_forwards(answer6)
