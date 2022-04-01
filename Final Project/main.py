import csv
import codecs
import sys
clients = ""
clients_file = 'list_clients.csv'


def readaddFile():
    global clients #Se trae variable clients de todo código
    with codecs.open(clients_file, 'r','utf-8') as clientswfile:
        clientsw = csv.reader(clientswfile,delimiter=',')
        # print(f"Type of clientsw: {type(clientsw)}") Type of clientsw: <class '_csv.reader'>
        next (clientsw, None)
        for row in clientsw:
            clients = clients + row[0] + ', '


def _get_client_name():
    client_name_inter = None
    while not client_name_inter: #Significa que mientras que no tenga un nombre de cliente, seguirá preguntando
        client_name_inter = input("Introduce please the name of the client: \n Or write \'exit\' to comeback")
        if client_name_inter == 'exit':
            client_name_inter = None
            break
    if not client_name:
        sys.exit()
    return client_name_inter




def create_client(client_name):
    global clients # Indica que la variable clients está a nivel global
    if client_name not in clients:
        clients += client_name
        _addcomma()
    else:
        print("This client is already in the list of client\'s")


def client_error():
    print("That client doesn't exist yet, these are the clients that exist at this moment: ")
    list_clients()


def list_clients():
    global clients
    clientsshow = clients[:-2]
    print(f"{clientsshow} \n")


def update_client(client_name,updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace (client_name + ',' , updated_client_name + ',')
    else:
        client_error()


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace (client_name + ',' , "")
    else:
        client_error()


def search_client(client_name):
    global clients
    clients_list = clients.split(', ')
    for cliente in clients_list:
        if cliente != client_name:
            continue # Indica "No ejecutes nada más dentro de esta iteración, ve a la siguiente" Break sale de la iteración
        else:
            return True


def _addcomma():
    global clients
    clients += ', '


def _print_welcome():
    print('*' * 50)
    print("Welcome to platzi ventas")
    print('*' * 50)
    print("\nWhat do you want to do, today? \n ")
    print('[C]reate client')
    print('[R]ead clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('Or please, write \'exit\' to break the program \n')

readaddFile()

while True:

    if __name__ == '__main__':
        _print_welcome()
        command = input("").upper()
        print("\n")
        if command == 'C':
            client_name = _get_client_name()
            create_client(client_name)
            list_clients()
        elif command == 'R':
            list_clients()
        elif command == 'U':
            client_name = _get_client_name()
            updated_client_name = input('What is the updated client name? ')
            update_client (client_name, updated_client_name)
            # Primero escribir el código y después implementar la función
            list_clients()
        elif command == 'D':
            client_name = _get_client_name()
            delete_client(client_name)
            list_clients()
        elif command == 'S':
            client_name = _get_client_name()
            found = search_client(client_name)            
            if found == True:
                print("This client exist")
            else:
                print("The client: {} is not in our client\'s list".format(client_name)) #Las llaves son un placeHolder son un espacio para dejar nuevos valores posteriormente
        elif command == 'EXIT':
            sys.exit()
        else:
            print("Invalid command")
        # list_clients()
        # create_client('Alvaro')