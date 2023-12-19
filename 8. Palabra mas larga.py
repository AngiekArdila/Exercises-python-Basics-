
cantidad=int(input("Ingresa la cantidad de palabras que usaras"))
length_str=0 
mayor=0
palabra1=str("")


while cantidad>0:
    cantidad=cantidad-1
    palabra=str(input("Escribe tu palabra:"))
    length_str=len(palabra)
    print(length_str) 
    if length_str>mayor:
        mayor=length_str
        print("Esta es la palabra mas larga hasta el momento: "+palabra)
        

    
    
