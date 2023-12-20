palabra = input("Ingresa tu palabra: ")
palabra2 = input("Ingresa tu palabra: ")

longitud1 = len(str(palabra))
print("Longitud de la primera palabra:", longitud1)

longitud2 = len(str(palabra2))
print("Longitud de la segunda palabra:", longitud2)

diferencia = int(longitud2 - longitud1)
print("la segunda palabra es mas larga por: ", str(diferencia))
diferencia2= int(longitud1-longitud2)
print("la primera palabra es mas larga por: ",str(diferencia2))

if longitud1 < longitud2:
    print("La segunda palabra",palabra2,"es más larga por", str(diferencia), "caracteres.")
if longitud1 >longitud2:
    print("la primera palabra: ", palabra,"es mas larga por",str(diferencia2),"caracteres.")