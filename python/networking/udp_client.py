import socket

SERVER_IP   = '127.0.0.1'
SERVER_PORT = 5005

MESSAGE     = b'Hello world!' # needs to be a byte string

# .AF_INET denotes IPv4
# stack overflow answer: https://stackoverflow.com/questions/1593946/what-is-af-inet-and-why-do-i-need-it#:~:text=AF_INET%20is%20an%20address%20family,that%2# it is an address family (AF) that is used to designate the type of addresses that your socket can
# communicate with (in this case, IPv4). When you create a socket, you have to specify its address
# family, and then you can only use addresses of that type with the socket. The Linux kernel, for
# example supports 29 other address families sush as UNIX (AF_UNIX) sockets and IPX (AF_IPX), and
# also communications with IRDA and Bluetooth (AF_IRDA and AF_BLUETOOTH, but it is doubtful you'll
# use these at such a low level). AF_INET6 is for IPv6 addresses.

# .SOCK_STREAM is for TCP
# .SOCK_DGRAM is for UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # internet, UDP

# tcp uses .send, udp uses .sendto
# udp client will send messages all day regardless if the server actually recieves them or not
s.sendto(MESSAGE, (SERVER_IP, SERVER_PORT))
print(f'SERVER target IP: {SERVER_IP}')
print(f'SERVER target port: {SERVER_PORT}')
print(f'Message: {MESSAGE}')
