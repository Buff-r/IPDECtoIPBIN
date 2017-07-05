#!/usr/bin/python
#IPDECtoIPBIN
#Made By Buff_r (JD)
import sys

print "IPDECtoIPBIN v1.1"
print "Made by Buff_r (JD)"
try:
	ip = sys.argv[1]
except IndexError:
	print "Example: ipdectoipbin.py <IP Address>"
	quit()

ip_byte_list = []
ip_byte_bin = []
ip_split = ip.split('.')
for i in ip_split:
	ip_byte_list.append(i)
	i = int(i)
	if i > 255:
		print "Error: Illegal byte in address."
		quit()
	else: 
		pass
	dec2bin = "{0:b}".format(i)
	bitcount = len(dec2bin)
	if bitcount < 8:
		zerobits = 8-bitcount
		zerobits = '0'*zerobits
		dec2bin = zerobits+dec2bin
	ip_byte_bin.append(dec2bin)
decbyte1 = ip_byte_list[0]
decbyte2 = ip_byte_list[1]
decbyte3 = ip_byte_list[2]
decbyte4 = ip_byte_list[3]
binbyte1 = ip_byte_bin[0]
binbyte2 = ip_byte_bin[1]
binbyte3 = ip_byte_bin[2]
binbyte4 = ip_byte_bin[3] 
ipbin = binbyte1+'.'+binbyte2+'.'+binbyte3+'.'+binbyte4

#Output
print decbyte1 + ' -> ' +  binbyte1
print decbyte2 + ' -> ' +  binbyte2
print decbyte3 + ' -> ' +  binbyte3
print decbyte4 + ' -> ' +  binbyte4
print '_'*40
print 'DEC: ', ip
print 'BIN: ', ipbin
