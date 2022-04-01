import csv
import codecs
clients = ""
clients_file = 'list_clients.csv'
def readFile():
    global clients #Se trae variable clients de todo código
    with codecs.open(clients_file, 'r','utf-8') as clientswfile:
        clientsw = csv.reader(clientswfile,delimiter=',')
        # print(f"Type of clientsw: {type(clientsw)}") Type of clientsw: <class '_csv.reader'>
        next (clientsw, None)
        for row in clientsw:
            clients = clients + row[0] + ', '
    # print(clients)
readFile()