from scapy.all import *
import base64
chunk=""
readthis = PcapReader('icmp-ctf.pcap')        
readthis = PacketList([p for p in readthis if p[IP].src == '192.168.56.210']) #过滤规则 
for p in readthis:
    ip= IP(p[Raw].load) #提取load部分
    chunk=chunk + str(ip)[-33:-1] #最后32位拼接
target= open('flag.gif','wb')
target.write(base64.b64decode(chunk)) #base64解码
target.close()