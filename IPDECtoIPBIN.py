#IPDECtoIPBIN
#Made By Buff_r (JD)
#from decimal import *

print "IPDECtoIPBIN"
print "Made by Buff_r (JD)"
ip = raw_input("IP: ")

ip_byte_list = []
ip_byte_bin = []
ip_split = ip.split('.')
for i in ip_split:
	ip_byte_list.append(i)
	if i > "255":
		print "Error: Illegal byte in address."
		quit()
	else: 
		pass
	i = int(i)
	dec2bin = "{0:b}".format(i)
	ip_byte_bin.append(dec2bin)
decbyte1 = ip_byte_list[0]
decbyte2 = ip_byte_list[1]
decbyte3 = ip_byte_list[2]
decbyte4 = ip_byte_list[3]
binbyte1 = ip_byte_bin[0]
binbyte2 = ip_byte_bin[1]
binbyte3 = ip_byte_bin[2]
binbyte4 = ip_byte_bin[3] 

#Output
print decbyte1 + ' -> ' +  binbyte1
print decbyte2 + ' -> ' +  binbyte2
print decbyte3 + ' -> ' +  binbyte3
print decbyte4 + ' -> ' +  binbyte4
