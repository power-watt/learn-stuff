import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005

BUFFER_SIZE = 1024

# .AF_INET denotes IPv4
# stack overflow answer: https://stackoverflow.com/questions/1593946/what-is-af-inet-and-why-do-i-need-it#:~:text=AF_INET%20is%20an%20address%20family,that%20type%20with%20the%20socket.
# it is an address family (AF) that is used to designate the type of addresses that your socket can
# communicate with (in this case, IPv4). When you create a socket, you have to specify its address
# family, and then you can only use addresses of that type with the socket. The Linux kernel, for
# example supports 29 other address families sush as UNIX (AF_UNIX) sockets and IPX (AF_IPX), and
# also communications with IRDA and Bluetooth (AF_IRDA and AF_BLUETOOTH, but it is doubtful you'll
# use these at such a low level). AF_INET6 is for IPv6 addresses.

# .SOCK_STREAM is for TCP
# .SOCK_DGRAM is for UDP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER_IP, SERVER_PORT)) # both tcp and udp server socket use .bind()

s.listen(5) # TCP listens and accepts

try:
    while True:
        (client_socket, client_address) = s.accept()
        print(f'accept client socket from {client_address}')

        # receive message over tcp
        # tcp uses .recv, udp uses .recvfrom
        data = client_socket.recv(BUFFER_SIZE)
        print(f'recv: \t {data}')

        # send message over tcp
        # tcp uses .send, dup uses .sendto
        response = b'Hello world back from server'
        client_socket.send()
        print(f'send: \t {response}')

        # close client socket
        print('close client socket')
        client_socket.close()
except KeyboardInterrupt:
    # close server socket 
    print('close server socket')
    s.close()
