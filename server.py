import socket
import sys

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создаем новый сокет
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #настраиваем его на принудительную реассоциацию с ip клиента в случае перезапуска
    sock.bind((interface, port)) #говорим, что будет слушать входящие соединения по адресу и порту
    sock.listen(1) #число клиентов в очереди
    while True:
        client, addr = sock.accept() #ждем соединения от клиента
        print('Got connection from: ',addr)
        message = recvall(client)
        print('Received from client: ')
        client.sendall(b'Hello, client\r\n')
        client.close()

def client(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    print('My address: ', sock.getsockname())
    sock.sendall(b'Hello, srv\r\n')
    message = recvall(sock)
    print('Server answer: ',message)
    sock.close()

##def recvall(sock, length):
##    data = b''
  ##  while len(data)<length:
    ##    part = sock.recr(length-len(data))
      ##  if not part:
        ##    raise Exception("Boom!")
        ##data += part
   ## return data

def recvall(sock):
    data = b''
    while True:
        part = sock.recv(1024)
        data += part
        part = part.decode()
        if part.endswith('\r\n'):
            break
    return data

if __name__ == "__main__":
    print(sys.argv)
    f = {
        'server': server,
        'client': client
    }[sys.argv[1]]
    host,port = '127.0.0.1', 1060
    if len(sys.argv)>2:
        host = sys.argv[2]
        if len(sys.argv)>2:
            port = int(sys.argv[3])
    f(host, port)