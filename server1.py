import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 8083))
print('Начинаем наш диалог')
while True:
    data, addr = sock.recvfrom(1024)
    msg = data.decode('utf-8')
    if msg == 'exit':
        print("Другой участник чата завершил общение")
        break
    print('сообщение клиента: ' + msg)
    replymsg = input('Ответить: ')
    sock.sendto(replymsg.encode('utf-8'), addr)
sock.close()