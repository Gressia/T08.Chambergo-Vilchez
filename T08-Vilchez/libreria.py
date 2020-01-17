#EJERCICIO 1
#Funcion : valida si es un nombre de persona
#Parametros : strNombre => Nombre de persona
#Retorna : bool
def validar_nombre(strNombre):
    #tipo de dato es de strNombre es str
    #la longitud de la cadena es menos de 4
    if( isinstance(strNombre,str) ):
        if ( len(strNombre) >= 4):
            return True  # Es un nombre valido
        else:
            return False # Insuficientes caracteres
    else:
        return False    # no es una str
#fin_validar_nombre

#EJERCICIO 2
# Funcion   : validar la letra
# Parametros: strLetra => inicial Letra
# Retorna   : bool
def validar_la_letra(strLetra):
    if ( strLetra== 'A' or strLetra== 'B'):
        return True
    else:
        return False
#fin_validar_la_letra

#EJERCICIO 3
# Funcion   : Verifica si intNum es un entero
# Parametros: intNum => Numero entero
# Retorna   : bool
def validar_entero(intNum):
    if ( intNum != int):
        return True
    else:
        return False
#fin_validar_entero

#EJERCICIO 4
# Funcion : Es hexadecimal
#Parametros : strNum

def es_hexadecimal(strNum):
    # 1. strNum puede ser un numero de 0-9 o letras de A-F
    if( strNum == "0" or strNum == "1" or strNum == "2" or
        strNum == "3" or strNum == "4" or strNum == "5" or
        strNum == "6" or strNum == "7" or strNum == "8" or
        strNum == "9" or strNum == "A" or strNum == "B" or
        strNum == "C" or strNum == "D" or strNum == "E" or
        strNum == "F"):
        return True
    else:
        # si no es ningun numero 0-9 ni letra de a-z
        return False
#fin_es_hexadecimal

#EJERCICIO 5
#Funcion : validar rgb
#Parametros : strRgb

def validar_rgb(strRgb):
    # 1. strRgb es una cadena de 8 caracteres
    # 2. El primer caracter de strRgb es el signo #
    # 3. Iterar cada caracter restante y verificar si es hexadecimal
    if ( len(strRgb) != 8 ):
        return False
    if (strRgb[0] != "#" ):
        return  False

    for caracter in strRgb[1:]:
        if ( es_hexadecimal(caracter) == False ):
            return False
        #fin_if
    #fin_for
#fin_validar_rgb

#EJERCICIO 6
#Funcion : es bit
#Parametro : strBit
def es_bit(strBit):
      # 1. strBit puede ser la cadena '0' o '1'
      if( strBit == '0' or strBit == '1' ):
          return True
      else:
          return False
#fin_es_bit

#EJERCICIO 7
#Funcion : es byte
#Parametro : strByte
def es_byte(strByte):
    # 1. strByte es una cadena de 9 caracteres
    # 2. Iterar cada caracter y verificar si es un bit
    if ( len(strByte) != 9 ):
        return False

    for caracter in strByte:
        if ( es_bit(caracter) ==False ):
            return False
        #fin_if
    #fin_for
    return True
#fin_es_byte

#EJERCICIO 8
#Funcion: es sexo valido
#Parametro: strSexo
def es_sexo_valido(strSexo):
    # 1. convertir strSexo en Mayusculas
    # 2. Si strSexo es igual a 'M' o 'F' retornar True , caso contrario: False
    strSexo == strSexo.upper()
    if(strSexo == 'M' or strSexo == 'F'):
        return True
    else:
        return False
    #fin_if
#fin_es_sexo_valido

#EJERCICIO 9
#Funcion : calificar
#Parametro: strProm
#Retorna : # 1. prom=20 => Excelente
#          # 2. 15-19  =>  Bien
#          # 3. 10-14 => Regular
#          # 4. 5-9  => Bajo
#         # 5. 0-4  => Muy Bajo
def calificar(prom):
    if(prom == 20):
        return "Excelente"
    if(prom >= 16 and prom <= 19):
        return "Bien"
    if(prom >= 11 and prom <= 14):
        return "Regular"
    if(prom >= 4 and prom <= 9):
        return "Bajo"
    if(prom >= 0 and prom <= 4):
        return "Muy Bajo"
#fin_calificar


#EJERCICIO 10
#Funcion : area triangulo
#Parametro : base x altura
def area_triangulo(base, altura):
    resultado=(base*altura)/2
    return resultado
#fin_area_triangulo


#EJERCICIO 11
#Funcion : producto
#Parametro: pr
#Retorna : mayusculas
def producto(pr):
    if(pr=="gelatina"):
        return pr.upper()
    else:
        return pr
#fin_producto

#EJERCICIO 12
#Funcion : sumar
#Parametro : n1,n2
#Retorna : resultado
def sumar(n1,n2):
    resultado=n1+n2
    return resultado

#fin_sumar

#EJERCICIO 13
#Funcion : cris
#Parametro : cr
#Retorna : replace
def cris(cr):
    if(cr=="sonrisa"):
        return cr.strip()
    else:
        return cr
#fin_cris

#EJERCICIO 14
#Funcion: definir
#Parametro : br
#Retorna : upper
def definir(br):
    if(br=="BETZY"):
        return br.lower()
    else:
        return br
#fin_definir

#EJERCICIO 15
#Funcion : yo
#Parametro : tu
#Retorna : lower
def yo(tu):
    if(tu=="cariño"):
        return tu.upper()
    else:
        return tu
#fin_yo
