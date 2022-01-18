import socket

UDP_IP   = '127.0.0.1'
UDP_PORT = 5005
MESSAGE  = b'Hello world!' # needs to be a byte string

print(f'UDP target IP: {UDP_IP}')
print(f'UDP target port: {UDP_PORT}')
print(f'Message: {MESSAGE}')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # internet, UDP

s.sendto(MESSAGE, (UDP_IP, UDP_PORT))
