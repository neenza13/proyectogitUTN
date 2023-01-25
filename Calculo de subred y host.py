def convierte_ip_a_binario():
    byte=[0,0,0,0]
    primerbyte = 0
    ip_binaria=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    for i in range(1,5):
        while(True):
            try:
                numero=int(input("Cual es tu byte numero "+str(i)+": "))
                if primerbyte ==1:
                    primerbyte+=1
                    if numero >= 128 and numero <=191:
                        byte[i-1]= numero    
                        break
                    else:
                        print("Escribe solo numeros entreros")
                if numero >= 0 and numero <=255:
                    byte[i-1]= numero    
                    break
                else:
                    print("Escribe solo numeros entreros")
            except:
                print("Tu direccion debe de ser entre 128 y 191")
    print("Tu direccion es la siguiente: ", *byte,sep='.',end=""+"\n")
    byte1 = byte[0]
    for i in range(0,4):
        if byte[i]>=128:
            ip_binaria[i][0]=1
            byte[i]-= 128
        if byte[i]>=64:
            ip_binaria[i][1]=1
            byte[i]-= 64
        if byte[i]>=32:
            ip_binaria[i][2]=1
            byte[i]-= 32
        if byte[i]>=16:
            ip_binaria[i][3]=1
            byte[i]-= 16
        if byte[i]>=8:
            ip_binaria[i][4]=1
            byte[i]-= 8
        if byte[i]>=4:
            ip_binaria[i][5]=1
            byte[i]-= 4
        if byte[i]>=2:
            ip_binaria[i][6]=1
            byte[i]-= 2 
        if byte[i]>=1:
            ip_binaria[i][7]=1
            byte[i]-= 1
    print (byte1)
    return(ip_binaria,byte1)
def calculodehost (ip,salto):
    host =[]
    c = 0
    salto = salto-1
    print ("El prefijo es: ", salto)
    for x in range (4):
        for x2 in range (8):
            if c >= salto:
                host.append(ip[x][x2])
            c+=1
        hostdec="".join(map(str, host))
    print ("El host en binario es: ", *host)
    print ("En decimal es: ",int (hostdec,2))
def calculosubred (ip,salto):
    subred = []
    salto = salto -1
    if ip[0][0]==0:
        c = 8
        clase ="A"
    if ip [0][0]==1 and ip [0][1]==0:
        c = 16
        clase = "B"
    if ip [0][0]==1 and ip [0][1]==1:
        c = 24
        clase = "C"
    for x in range (1,4):
        for x2 in range (8):
            if clase == "A":
                if c<=salto:
                    subred.append(ip [x][x2])
                    c+=1
            elif clase == "B":
                if c<=salto:
                    subred.append(ip [x+1][x2])
                    c+=1
            elif clase == "C":
                if c<=salto:
                    subred.append(ip [x+2][x2])
                    c+=1
        subreddec = "".join(map(str,subred))
    print ("La subred en binario es: ",*subred)
    print ("La subred en decimal es: ", int (subreddec,2))
def clases(by1):
    while(True):
        try:
            mas=int(input(f"\n Indica el numero de prefijo entre 9 y 30: "))
            if by1>=192 and by1<=223:
                if mas>=25 and mas<=30:
                    print ("Tu IP es clase C")
                    break
                else:
                    print ("El prefijo no esta Dentro de la Clase")
            elif by1>=128 and by1<=191:
                if mas>=17 and mas<=24:
                    print ("Tu IP es clase B1")
                    break
                elif mas>=25 and mas<=30:
                    print ("Tu IP es clase B2")
                    break
                else:
                    print ("El prefijo no esta Dentro de la Clase")
            elif mas>=1 and mas>=8 and mas<=32:
                if by1>=1 and by1<=126:
                    if mas>=9 and mas<=16:
                        print ("Tu IP es clase A1")
                        break
                    elif mas>=17 and mas<=24:
                        print ("Tu IP es clase A2")
                        break
                    elif mas>=25 and mas<=30:
                        print ("Tu IP es clase A3")
                        break
                    else:
                        print ("El prefijo no esta Dentro de la Clase")
        except:
            print ("Todo esta mal")
    return (mas)
ip, octeto1 = convierte_ip_a_binario()
salto = clases(octeto1)
calculodehost(ip,salto)
calculosubred (ip,salto)
"""
Segundo Parcial Práctico AID II
Vence el 31 de octubre de 2022 23:59
Instrucciones
Crea un programa que dada IP y una máscara obtenga el No. de host y No. subred
La IP debe ser validada entre clase A, B y C
La máscara debe ser validada para la Clase con la que trabaja, no debe de ser menor que la máscara por defecto.
La operaciones se deben de hacer en binario.
Usa funciones para cada acción a realizar
Muestra en pantalla los resultados en decimal y binario
"""