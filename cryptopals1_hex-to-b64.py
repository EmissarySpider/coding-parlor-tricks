# Cryptopals Challenge 1: https://cryptopals.com/sets/1/challenges/1
# Convert a hex string to base64, operating only on bytes
# No b64 library or equivalent!

import math
hexstr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# create map/dict of hex characters to binary

h2b_map = {'0':"0000", '1':"0001", '2':"0010", '3':"0011", '4':"0100", '5':"0101", '6':"0110", '7':"0111", '8':"1000", '9':"1001", 'a':"1010", 'b':"1011", 'c':"1100", 'd':"1101", 'e':"1110", 'f':"1111"}


def conv_hex_to_bin(string):
    int_binstr = ''
    for hexchar in hexstr:
        binval = h2b_map[hexchar]
        int_binstr = int_binstr+binval
    return int_binstr

binstr = conv_hex_to_bin(hexstr)

# split binary string into 4 pieces cotaining 6 bits each
def add_spaces(bin_string, i_spaces):
    instrlen = len(bin_string)
    str_w_spaces = ""
    ct = 0
    while ct<=instrlen:
        curr_chunk = bin_string[ct:ct+i_spaces]+' '
        str_w_spaces = str_w_spaces+curr_chunk
        ct+=i_spaces
    return str_w_spaces
with_spaces = add_spaces(binstr, 6)

# convert the binary string to decimal
decimal_list = []
def convert_binary2dec(bin_string):
    bin_list = bin_string.split(' ')
    for bin_group in bin_list:
        if bin_group == "": continue
        ct = 5
        dec_sum = []
        group_len = len(bin_group)
        for i in range(0,group_len): # walk group and get each bit's value and convert
            bin_bit = float(bin_group[i])
            if bin_bit == 0.0 and ct > 0: 
                ct -=1
                continue
            """
            bin to decimal formula aka decify: 
            (bin_group[5] × 2⁵) + (bin_group[4] × 2⁴) + 
            (bin_group[3] × 2³) + (1 × 2²) + (1 × 2¹) + (0 × 2⁰)
            """
            decify = bin_bit * (math.pow(2.0,ct))
            dec_sum.append(decify)
            if ct > 0:
                ct-=1
            elif ct == 0:
                total = sum(dec_sum)
                decimal_list.append(int(total))
    return
convert_binary2dec(with_spaces)

# compare each decimal against each character in reference string of base64 characters
def convert_decimal_to_b64(decimals):
    base64_char_array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    b64_encoded_str = ''
    for dec_val in decimal_list:
        bchar = base64_char_array[dec_val]
        b64_encoded_str+=bchar
    return b64_encoded_str

answer = convert_decimal_to_b64(decimal_list)
print(answer)

# output should be SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
