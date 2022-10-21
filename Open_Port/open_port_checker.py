import socket
import subprocess
import sys

subprocess.call("cls", shell=True)

print("[+] For Host Scane Enter 1")
print("[+] For Ip Scane Enter 2")
choice = input(">> ")

if choice == "1":
	print("Please Enter Formate Like That 'www.Domain_name.com'")
	host = input("Enter The Host Name :-")
	host_ip = socket.gethostbyname(host)
elif choice == "2":
	print("Please Enter Formate Like That 'xxx.xxx.xxx.xxx'")
	host_ip = input("Enter The IP ADDR :-")

print("*"*60)
print("Scanning port")
print("*"*60)

try:
	for port in range(1,1025):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect_s = server.connect_ex((host_ip, port))

		if connect_s == 0:
			print(f"{port} Is Open")
		server.close()

except KeyboardInterrupt:
	sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server. Please TRY Again")
    sys.exit()
