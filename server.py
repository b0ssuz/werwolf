import select
import socket
import sys
from threading import Thread
from RollenGut import *
from RollenBoese import *


def main():
    serverThread = Thread(target=server) # Erstellt Thread für den Server
    serverThread.start() # startet den Server-(Thread)
	


def startGame():
    """ Funktion um eine Spiel Session zu starten """
	print("game started!")

def server():
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000) #muss noch angepasst werden
    print('starting up on %s port %s' % server_address, file=sys.stderr)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen()
    button_pressed = False
    while True:
        # Wait for a connection
        print('waiting for a connection', file=sys.stderr)
        connection, client_address = sock.accept()
        client = connection.getpeername()[0]
        print('Client: ', client, file=sys.stderr)
        d = {}
        playernumber = 0
        try:
                print('connection from', client_address, file=sys.stderr)

                print(connection.getpeername())

                # Set non-blocking
                connection.setblocking(0)

                data = ""
                ready = select.select([connection], [], [], 5) # wait 5 secs
                if ready[0]:
                    data = connection.recv(4096) # Dirty! We hope to catch a complete request from the client here...

                if data:
                    print('received "%s"' % data, file=sys.stderr)
                    if client not in d.keys():
                        d[client] = playernumber
                        playernumber += 1
                    responseHead = 'HTTP/1.1 200 OK\r\n'
                    if data[:11] == b'GET /active':
                        button_pressed = True
                    refresh = '<head><meta http-equiv="refresh" content="15"><title>Werwolf</title></head>'
                    if button_pressed:
                        response = '<body><h1>%s</h1></body>' %str(d[client])
                        if d[client] == 0:
                            response = '<body><h1>Hallo Spieler (Admin)</h1><form action="/active"><input type="submit" value="Start Game"></form></body>' 
                            # if "Start Game"- Button pressed startGame()
                    else:
                        response = '<body><h1>Hallo Spieler </h1><form action="/active"><input type="submit" value="Start"></form></body>'
                        response = '<body><h1>Hallo Spieler</h1><form action="/active"><input type="submit" value="Start"></form></body>'
                    response = '<html>' + refresh + response + '</html>'
                    responseHead += 'Content-length: ' + str(len(response)) + '\r\n'
                    response = responseHead + "\r\n" + response
                    #print(response)
                    connection.sendall(response.encode())
                else:
                    print('no more data from', client_address, file=sys.stderr)

        finally:
            # Clean up the connection
            print('close connection', file=sys.stderr)
            connection.close()

if __name__ == "__main__":
	main()
