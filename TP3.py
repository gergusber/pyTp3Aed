
#Declaración de un registro con su constructor.
class Canciones:
    #Constructor
    def __init__(self, tit = 'asignar', alb = 'asignar', ban = 'asignar', lang = 0, gen = 0, repr = 0):
        self.titulo = tit
        self.album = alb
        self.banda = ban
        self.idioma = lang
        self.genero = gen
        self.reproducciones = repr

def write(canciones):
    print('Titulo:', canciones.titulo, end=' ')
    print('Album:', canciones.album, end=' ')
    print('Banda:', canciones.banda, end=' ')
    print('Idioma:', canciones.idioma, end=' ')
    print('Genero:', canciones.genero, end=' ')
    print('Reproducciones:', canciones.reproducciones, end=' ')
    print("")

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese cantidad de canciones a cargar (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...\n'
                                                  '>>>Ingrese: ')

    return n

def read(canciones):
    n = len(canciones)
    for i in range(n):
        lan = -1
        gen = -1
        repr = -1
        tit = input('Título de la canción: ')
        alb = input('Nombre del álbum: ')
        ban = input('Nombre de la banda: ')
        while lan < 0 or lan > 3 :
            lan = int(input('Ingrese el idioma del 0 al 3:(0: inglés, 1: español, 2: francés, 3: otros) '))
        while gen < 0 or gen > 9:
            gen = int(input('Ingrese el género del 0 al 9: '))
        while repr < 0:
            repr = int(input('Ingrese la cantidad de reproducciones: '))

        print()

        canciones[i] = Canciones(tit, alb, ban, lan, gen, repr)

def sort(canciones):
    n = len(canciones)
    for i in range(n-1):
        for j in range(i+1, n):
            if canciones[i].titulo > canciones[j].titulo:
                canciones[i], canciones[j] = canciones[j], canciones[i]
    return canciones

def display(canciones):
    n = len(canciones)
    for i in range(n):
        write(canciones[i])

def display_Test(canciones, x):
    n = len(canciones)
    print('Canciones con cantidad de reproducciones >=', x, '):')
    for i in range(n):
        if canciones[i].reproducciones >= x:
            write(canciones[i])

def buscarEnDiscos(nombDisco,canciones):
    n = len(canciones)
    listaAlbums = []
    for i in range(n):
        if(nombDisco in canciones[i].album):
            listaAlbums.append(canciones[i])
    return listaAlbums

def filtroPorNombreDisco(canciones):
    nombDisco = input('Ingrese el nombre del disco: ')
    while(nombDisco == '' or nombDisco == None ):
        nombDisco = input('Ingrese el nombre del disco: ')
    return buscarEnDiscos(nombDisco,canciones)

def test():
    # cargar cantidad de canciones
    n = validate(0)

    canciones = n * [None]

    # cargar el arreglo por teclado...
    print('\nCargue los datos de las canciones:')
    read(canciones)
    print()

    opcion = 0
    while opcion < 1 or opcion > 8:
        opcion = int(input("ERROR /// Se pidió que ingrese entre 1 y 8.\n>>>Ingrese:  "))

        if opcion == 1:
            print('\nCanciones ordenadas alfabeticamente: ')
            display(sort(canciones))
        elif opcion == 2:
            display(filtroPorNombreDisco(canciones))
        

test()
