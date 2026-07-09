def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_autor(autor):
    return autor.strip() != ""
   
def validar_genero(genero):
    return genero.strip() != ""

def validar_ano(ano):
    return ano.isdigit() > 0

def validar_editorial(editorial):
    return editorial.strip() != ""

def validar_novedad(novedad):
    return novedad in [True, False]

def validar_multa(multa):
    return multa > 0

def validar_copias(copias):
    return copias >= 0

libros = {
'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019,
'AndesPress', False],
'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023,
'CodeBooks', True],
'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral',
False],
'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015,
'Cronos', False],
'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021,
'Orión', True],
'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores',
False],
}

prestamos = {
'L001': [500, 4],
'L002': [700, 0],
'L003': [300, 10],
'L004': [400, 2],
'L005': [600, 1],
'L006': [350, 6],
}

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Copias por género")
    print("2. Búsqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6. Salir")
    print("=====================================")

def leer_opcion(opcion):
    while True:
        opcion = input("Ingrese una opcion: ")
        if opcion.isdigit() and 1 <= int(opcion) <= 6:
            break
        else:
            print("Error. Debe ser un numero entre el 1 y el 6")
         

def copias_genero(genero):
    total_copias = 0
    for cod, datos in libros.items():
        if datos[1].lower() == genero.lower():
            total_copias += prestamos[cod][1]
    print(f"Las copias disponibles son: {total_copias}")        
        
           
def busqueda_multa(multa_min, multa_max):
    resultados[]
    for cod, datos_op in prestamos.items():
        multa = datos_op[0]
        copias = datos_op[1]
        if multa_min <= multa <= multa_max and copias >0:
            cantidad_multa = planes[cod][0]
            resultados.append(f"{cantidad_multa}")


    


def actualizar_multa(codigo , nueva_multa):
    cod.upper()

def agregar_libro(codigo, titulo, autor, genero, ano, es_novedad, precio_multa, copias_disponibles):
