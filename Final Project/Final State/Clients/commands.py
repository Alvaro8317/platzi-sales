import click


@click.group() #Lo que hace group es convertir client en otro decorador
def clients():
    """Manages the clients lifecycle""" #Descripción de lo que hace
    pass


@click.command()
@click.pass_context()
def create(ctx,name,company,email,position):
    """Creates a new client"""
    pass

@click.command()
@click.pass_context()
def list(ctx): #Context es lo que se acaba de inicializar como un diccionario vacío
    """List all clients"""
    pass


@click.command()
@click.pass_context()
def update(ctx,client_uid):
    """Updates a client"""
    pass


@click.command()
@click.pass_context()
def delete(ctx,client_uid):
    """Deletes a client"""
    pass

all = clients
