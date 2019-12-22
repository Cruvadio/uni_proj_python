import collections

     
def shex(n):
    bits = bin(n)[2:]
    i=0
    while (len(bits) + i )%6 != 0:
        i+=1
    bits = "0"*i + bits
    i = 0
    res = ""
    for i in range(0, len(bits), 6):
         res += chr(int("0b" + bits[i:i+6], 2) + 32)
    
    return res
    
def xehs(s):
    res = 0
    for i, k in enumerate(reversed(s)):
        res += (ord(k) - 32) * 64 ** i
    return res
	
def encode (txt):
    comm = sorted(sorted(collections.Counter(txt).most_common(), key=lambda x: x[0], reverse=True), key=lambda x: x[1], reverse=True)
    string = ""
    for c in comm:
        string += c[0]
    d = dict()
    s = "0"
    for i, c in enumerate(string):
        d[c] = '1' * i + s
    bits = ""
    for t in txt: 
        bits += d[t]
    while len(bits) % 6 != 0:
        bits += s
    num = shex(int(bits, 2))
    return (len(txt), string, num)
    
    
def decode (length, char, code):
    d = dict()
    s = "0"
    for i, c in enumerate(char):
        d['1' * i + s] = c
    bits = bin(xehs(code))
    string = ""
    k = 2
    for i in range(length):
        num = ''
        while k < len(bits) and bits[k] != '0':
            num += bits[k]
            k += 1
        num += bits[k]
        k += 1
        string += d[num]
	
    return string
