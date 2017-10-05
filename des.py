PC1 = [ 
    57, 49, 41, 33, 25, 17,  9,
     1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29, 
    21, 13,  5, 28, 20, 12,  4, ]

PC2 = [ 
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8, 
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32, ]

P = [   
    16,  7, 20, 21,
    29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25, ]

NUM_OF_SHIFT = [
    1, 1, 2, 2, 
    2, 2, 2, 2, 
    1, 2, 2, 2, 
    2, 2, 2, 1, ]

IP = [  
    58, 50, 42, 34, 26, 18, 10,  2,
    60, 52, 44, 36, 28, 20, 12,  4,
    62, 54, 46, 38, 30, 22, 14,  6,
    64, 56, 48, 40, 32, 24, 16,  8,
    57, 49, 41, 33, 25, 17,  9,  1,
    59, 51, 43, 35, 27, 19, 11,  3,
    61, 53, 45, 37, 29, 21, 13,  5,
    63, 55, 47, 39, 31, 23, 15,  7, ]

IPI = [ 
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25, ]

E = [
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1, ]

S1 = [
    [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
    [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
    [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
    [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]]

S2 = [
    [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
    [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
    [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
    [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]]

S3 = [
    [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
    [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
    [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
    [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]]

S4 = [
    [ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
    [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
    [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
    [ 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]]

S5 = [
    [ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
    [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
    [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
    [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]]

S6 = [
    [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
    [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
    [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
    [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]]

S7 = [
    [ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
    [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
    [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
    [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]]

S8 = [
    [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
    [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
    [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
    [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]

SN = [S1, S2, S3, S4, S5, S6, S7, S8]


def padding(num, total):
    return format(num, '0%db' % total)


def join(list_of_str):
    return ''.join(list_of_str)


def left_shift(str_bin, total=1):
    return str_bin[total:] + str_bin[0:total]


def str_bin_to_hex(str_bin):
    partial = int(len(str_bin)/4)
    return join([format(int(str_bin[4*i:4*(i+1)] ,2), 'x') for i in range(partial)])


def str_bin_to_str_ascii(str_bin):
    partial = int(len(str_bin)/8)
    return join([format(int(str_bin[8*i:8*(i+1)] ,2), 'c') for i in range(partial)])


def hex_to_str_bin(hexa):
    return join([padding(int(c, 16), 4) for c in hexa])


def str_to_str_bin(txt):
    return join([padding(ord(c), 8) for c in txt])


def permutate(str_bin, table):
    return join([str_bin[i-1] for i in table])


def xor(sb1, sb2):
    pad = len(sb1) if len(sb1) > len(sb2) else len(sb2)
    sb_1 = int(sb1, 2)
    sb_2 = int(sb2, 2)
    result = sb_1 ^ sb_2
    return padding(result, pad)
    

class DES(object):

    
    def __init__(self, hex_mode=False):
        self.hex_mode = hex_mode
        
    
    def generate_subkeys(self, key):
        if self.hex_mode:
            bin_key = hex_to_str_bin(key)
        else:
            bin_key = str_to_str_bin(key)
            
        Cn = []
        Dn = []
        Kn = []
        KP = permutate(bin_key, PC1)

        Cn.append(KP[:28])
        Dn.append(KP[28:])
        
        for i in range(16):
            Cn.append(left_shift(Cn[i], NUM_OF_SHIFT[i]))
            Dn.append(left_shift(Dn[i], NUM_OF_SHIFT[i]))
            CnDn = Cn[i+1] + Dn[i+1]
            Kn.append(join([CnDn[i-1] for i in PC2]))
        
        return Kn
    
    
    def encrypt(self, message, key):
        if self.hex_mode:
            bin_key = hex_to_str_bin(key)
            bin_msg = hex_to_str_bin(message)
        else:
            bin_key = str_to_str_bin(key)
            bin_msg = str_to_str_bin(message)
            
        subkeys = self.generate_subkeys(key)
        encoded = self.encode(bin_msg, subkeys)
        
        if self.hex_mode:
            encoded = str_bin_to_hex(encoded)
        else:
            encoded = str_bin_to_str_ascii(encoded)
        
        return encoded
    
    
    def decrypt(self, chipper, key):
        if self.hex_mode:
            bin_key = hex_to_str_bin(key)
            bin_msg = hex_to_str_bin(chipper)
        else:
            bin_key = str_to_str_bin(key)
            bin_msg = str_to_str_bin(chipper)
            
        subkeys = self.generate_subkeys(key)
        encoded = self.encode(bin_msg, subkeys[::-1])
        
        if self.hex_mode:
            encoded = str_bin_to_hex(encoded)
        else:
            encoded = str_bin_to_str_ascii(encoded)
        
        return encoded
    
    
    def encode(self, str_bin, Kn):
        bip = permutate(str_bin, IP)
        
        Ln = []
        Rn = []
        
        Ln.append(bip[:32])
        Rn.append(bip[32:])

        for i in range(1,17):
            Ln.append(Rn[i-1])
            Rn.append(xor(Ln[i-1], self.fn(Rn[i-1], Kn[i-1])))
            
        RL = Rn[16] + Ln[16]
        
        return permutate(RL, IPI)
        
                  
    def fn(self, ri, ki):
        ei = permutate(ri, E)
        ei = xor(ki, ei)
        
        result = ''
        partials = [ei[6*i:6*(i+1)] for i in range(8)]
        
        for i, part in enumerate(partials):
            row = int(part[0] + part[-1], 2)
            col = int(part[1:5], 2)
            num = SN[i][row][col]
            result += padding(num, 4)
            
        result = permutate(result, P)
        
        return result
            