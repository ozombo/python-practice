import socket

website = input("Enter website address: ")

ip_address = socket.gethostbyname(website)
print(ip_address)