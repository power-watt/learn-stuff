import socket

UDP_IP   = '127.0.0.1'
UDP_PORT = 5005

BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((UDP_IP, UDP_PORT))

print(f'listening on {UDP_IP}:{UDP_PORT}')

while True:
    data, addr = s.recvfrom(BUFFER_SIZE)
    print('------------ receive --------------')
    print(data)
    print(addr)
