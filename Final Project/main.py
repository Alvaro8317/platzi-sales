import csv
import sys
import os
import codecs

clients_file = '.list_clients.csv' #El punto al principio indica que es un archivo oculto
clients_schema = ['Name', 'Company','Email','Position']
clients = []

# def readaddFile():
#     global clients #Se trae variable clients de todo código
#     with codecs.open(clients_file, 'r','utf-8') as clientswfile:
#         clientsw = csv.reader(clientswfile,delimiter=',')
#         # print(f"Type of clientsw: {type(clientsw)}") Type of clientsw: <class '_csv.reader'>
#         next (clientsw, None)
#         for row in clientsw:
#             clients = clients + row[0] + ', '

def _initialize_clients_from_storage():
    with codecs.open(clients_file,'r','utf-8') as file_r:
        reader = csv.DictReader(file_r, fieldnames=clients_schema) # Es una lista de las llaves que utilizará dictreader para construir los diccionarios
        for row in reader:
            clients.append(row)


def _save_client_storage():
    tmp_table = f'{clients_file}.tmp' #Se llevan los clientes a una tabla temporal porque una vez que se abre el archivo, no se puede escribirlo
    with codecs.open(tmp_table,'w', 'utf-8') as file_w:
        writer = csv.DictWriter(file_w, fieldnames=clients_schema)
        writer.writerows(clients)
    os.remove(clients_file)
    os.rename(tmp_table, clients_file)


def _get_client_field(field_name):
    fieldd = None
    while not fieldd:
        fieldd = input(f'What\'s the client {field_name}? ')
    return fieldd



def create_client(client):
    global clients # Indica que la variable clients está a nivel global
    print(client)
    if client not in clients:
        clients.append(client)
    else:
        print("This client is already in the list of client\'s")


def client_error():
    print("That client doesn't exist yet, these are the clients that exist at this moment: ")
    list_clients()


def list_clients():
    for idx, client in enumerate(clients): #La función enumerate brinda un conteo que para este caso es idx
        print(f"ID: {idx} | Nombre: {client['Name']} | Compañía: {client['Company']} | Correo: {client['Email']} | Posición: {client['Position']}")

def get_id(name):
    for i in clients:
        if name in i:
            print(i)


def update_client(idx,updated_client_name):
    global clients
    clients[idx] = updated_client_name


def delete_client(idx):
    global clients
    clients.pop(idx)


def search_client(client_name):
    global clients
    for client in clients:
        if client['Name'] != client_name:
            continue # Indica "No ejecutes nada más dentro de esta iteración, ve a la siguiente" Break sale de la iteración
        else:
            return True


def search_id(client_name):
    global clients
    for idx, client in enumerate(clients):
        if client['Name'] != client_name:
            continue
        else:
            return idx
    client_error()


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

# readaddFile()
_initialize_clients_from_storage()
while True:

    if __name__ == '__main__':
        _print_welcome()
        command = input("").upper()
        print("\n")
        if command == 'C':
            clientnew = {
                'Name': _get_client_field('Name'),
                'Company': _get_client_field('Company'),
                'Email': _get_client_field('Email'),
                'Position': _get_client_field('Position')
            }
            create_client(clientnew)
            _save_client_storage()
        elif command == 'R':
            list_clients()
        elif command == 'U':
            trysearch = _get_client_field('Name')
            trysearch = search_id(trysearch)
            if trysearch == None:
                print("Can not continue, does not exist that client")
                continue
            else:
                print("Now, please insert the information updated")
                clientupdate = {
                'Name': _get_client_field('Name'),
                'Company': _get_client_field('Company'),
                'Email': _get_client_field('Email'),
                'Position': _get_client_field('Position')
                }
                update_client(trysearch,clientupdate)
                _save_client_storage()
        elif command == 'D':
            trysearch = _get_client_field('Name')
            trysearch = int(search_id(trysearch))
            if trysearch == None:
                print("Can not continue, does not exist that client")
                continue
            else:
                delete_client(trysearch)
                _save_client_storage()
        elif command == 'S':
            client_name = _get_client_field('Name')
            found = search_client(client_name)            
            if found == True:
                print("This client exist")
            else:
                print("The client: {} is not in our client\'s list".format(client_name)) #Las llaves son un placeHolder son un espacio para dejar nuevos valores posteriormente
        elif command == 'EXIT':
            sys.exit()
        elif command == 'TEST':
            print(len(clients))
        else:
            print("Invalid command")
        