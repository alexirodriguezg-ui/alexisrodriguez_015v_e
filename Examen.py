def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_autor(autor):
    return autor.strip() != ""
   
def validar_genero(genero):
    return genero.strip() != ""

def validar_ano(ano):
    return ano.isdigit > 0

def validar_editorial(editorial):
    return editorial.strip() != ""
   

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

def leer_opcion():
    opcion = input("Ingrese una opcion ")

