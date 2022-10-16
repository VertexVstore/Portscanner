import socket
from IPy import IP

print("###############################################")
print("############# VERTEX V STORE ##################")
print("### Location: Muwayire Road(Behind IHK) #######")
print("### Address: vertexvstore@gmail.com ###########")
print("### Tel: +256 784 918 779 #####################")
print("###############################################")

def scan(target):
	converted_ip = check_ip(target)
	print('\n' + '[o_o] Scanning Target] ' + str(target))

	for port in range (1, 30000):
		scan_port(converted_ip, port)

def check_ip(ip):
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)

def get_banner(s):
	return s.recv(1024)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.settimeout(0.5)
		sock.connect((ipaddress, port))

		try:
			banner = get_banner(sock)
			print('[+] Open Port '+ str(port) + ' : ' + str(banner.decode().strip('\n')))
		except:
			print('[+] Open Port ' + str(port))
	except:
		pass

targets = input('[+] Split Targets With Comma, Enter To Scan:=> ')
if ',' in targets:
	for ip_add in targets.split(','):
		scan(ip_add.strip(' '))
else:
	scan(targets)