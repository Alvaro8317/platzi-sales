if __name__ == '__main__':
    import random
    def binarysearch(data, target, lowin, highin):
        if lowin > highin:
            return False
        mid = (lowin + highin) // 2 #División ceros
        # Hay 3 casos
        # 1. Uno en el que ya se encontró el índice
        # 2. Uno en el que el índice está por debajo de la mitad
        # 3. Uno en el que el índice está por encima de la mitad
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binarysearch(data,target,lowin,mid-1)
        elif target > data[mid]:
            return binarysearch(data,target,mid + 1 ,highin)
        else:
            print("Hay que llorar")

    listrandom = [random.randint(0,100) for a in range(10)]
    listrandom.sort() #Modifica directamente el array ordenándolo
    #listrandomsorted = sorted(listrandom) #Crea un nuevo array ya ordenado
    target = int(input("Write your number! "))
    found = binarysearch(listrandom,target,0,len(listrandom) - 1) #data, el array ya ordenado, target el número a encontrar, 0 el índice inferior y len(data) -1 como índice superior, se deja -1 para evitar un índice por fuera de la lista
    print(listrandom)