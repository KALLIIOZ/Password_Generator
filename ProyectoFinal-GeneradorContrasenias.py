import os
import random
import time

usuarios = {"OwenHerIs3492" : "odfHJ73w?z/",
            "ChavaUT9237" : "dEi)323pG*",
            "AlanPoCst6210" : "kP73¿lq@09",
            "MiguelNS1923" : "aoKQ62kd8-12#",
            "NestorZSeg0378" : "83!riTmv?32"}
 
historialDB = {
    "OwenHerIs3492" : {"oDFlwHj?340b" : "Cuenta de Google"},
    "ChavaUT9237" : {"9923344323" : "Cuenta de Tik Tok"},
    "AlanPoCst6210" : {"aKmdwPlfHT" : "Cuenta de Discord"},
    "MiguelNS1923" : {"ot*KyEr#932M" : "Cuenta de Instagram"},
    "NestorZSeg0378" : {"4593432343" : "Correo de Microsoft"}
}

signos = ['!','"','$','%','&','`','(',')','*','+',',','-','/',':',';','>','<','=','?','@','[',']','^','_','{','}','|','~' ]
numeros = ['0','1','2','3','4','5','6','7','8','9']
letrasMin = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letrasMay = []
for x in letrasMin:
    letrasMay.append(x.upper())
    
caracteres=[signos, numeros, letrasMin, letrasMay]
control = False
usuario = ""
funcion = 0
z = 0

def bienvenida():
    time.sleep(1)
    print("\n\t-------- GENERADOR AUTOMÁTICO DE CONTRASEÑAS --------\n")

def despedida():
    time.sleep(0.5)
    print("\n\n-Gracias por usar este programa. Vuelva pronto :)")

def finalizacion():
    time.sleep(0.5)
    print("\n\n-Programa finalizado. Hasta pronto.")

def iniciarSesion():
    nombre = password = str()
    c = 1
    time.sleep(1)
    for i in range(5):
        nombre = input("\n-Ingrese su nombre de usuario:")
        if (nombre in usuarios.keys()) == True:
            break
        elif i == 3:
            print("\n--> Solo tiene un intento más. De lo contrario, el programa dejará de ejecutarse por defecto. Vuelva a intentarlo.")
        elif i == 4:
            nombre = 'e'
            break
        else:
            print("\n--> Usuario ingresado no encontrado. Intente de nuevo.")
                
    time.sleep(0.5)
    if nombre != 'e':
        while True:
            password = input("-Ingrese su contraseña:")
            if usuarios[nombre] == password:
                break
            elif c == 4:
                print("\n--> Solo tiene un intento más. De lo contrario, el programa dejará de ejecutarse por defecto. Vuelva a intentarlo.\n")
                c += 1
            elif c == 5:
                password = 'e'
                break
            else:
                print("\n--> Contraseña ingresada no válida. Intente de nuevo.\n")
                c += 1
    else:
        password = 0
     
    time.sleep(0.5)
    if nombre != 'e' and password != 'e':
        print("\n\nAccediendo ...")
        time.sleep(4.5)
    return nombre, password

def metodoRellenado():
    metodo = str()
    c = 1
    time.sleep(0.7)
    print("\n------- MÉTODOS DE RELLENADO DE LA CONTRASEÑA -------\n\na) Manual\nb) Automático")
    while True:
        time.sleep(1)
        metodo = input("\n-Seleccione el método de rellenado para la contraseña a usar:")
        metodo = metodo.lower()
        if metodo == 'a' or metodo == 'b':
            break
        elif c == 4:
            print("\n--> Solo tiene un intento más. De lo contrario, la operación se detendrá. Vuelva a intentarlo.")
            c += 1
        elif c == 5:
            metodo = 'e'
            break
        else:
            print("\n--> Método seleccionado inexistente. Intente de nuevo.")
            c += 1
    
    return metodo

def tamanioCifrado():
    opcion = str()
    tamanio = int()
    c = 1
    
    time.sleep(0.7)
    
    print("\n------- DEFINIR TAMAÑO PARA LA CONTRASEÑA -------\n\na) Definir un tamaño manualmente\nb) Generar un tamaño aleatoriamente")
    while True:
        time.sleep(1)
        opcion = input("\n-Seleccione una opción:")
        opcion = opcion.lower()
        if opcion == 'a' or opcion == 'b':
            break
        elif c == 4:
            print("\n--> Solo tiene un intento más. De lo contrario, la operación se detendrá. Vuelva a intentarlo.")
            c += 1
        elif c == 5:
            opcion = 'e'
            break
        else:
            print("\n--> Método seleccionado inexistente. Intente de nuevo.")
            c += 1
            
    c = 1
    if opcion == 'a':
        while True:
            try:
                while True:
                    time.sleep(0.5)
                    tamanio = int(input("-Ingrese el tamaño que tendrá la contraseña:"))
                    if tamanio >= 8 and tamanio <= 16:
                        break
                    if c == 4:
                        print("\n--> SSolo tiene un intento más. De lo contrario, la operación se detendrá. Vuelva a intentarlo.\n")
                        c += 1
                    elif c == 5:
                        tamanio = 0
                        break
                    elif tamanio < 8:
                        print("\n--> El tamaño de la contraseña no puede ser menor a 8. Intente de nuevo.\n")
                        c += 1
                    else:
                        print("\n--> El tamaño de la contraseña no puede ser mayor a 16. Intente de nuevo.\n")
                        c += 1
                break
            except ValueError:
                if c == 4:
                    print("\n--> Solo tiene un intento más. De lo contrario, la operación se detendrá. Vuelva a intentarlo.\n")
                    c += 1
                elif c == 5:
                    tamanio = 0
                    break
                else:
                    print("\n--> Tipo de dato ingresado no válido. Intente de nuevo.\n")
                    c += 1
    elif opcion == 'b':
        time.sleep(0.7)
        print("\nGenerando tamaño aleatorio para la contraseña ...")
        time.sleep(2.5)
        tamanio = random.randint(8, 16)
    else:
        tamanio = 0
        
    return tamanio

def seguridad(tamanio):
    contrasenia = str()
    tipado = 'num'
    global funcion
    global z
    
    time.sleep(0.75)
    print("\n-------- CONTROL DE SEGURIDAD - CONTRASEÑAS NUMÉRICAS --------\n")
    while True:
        time.sleep(0.55)
        opsA1 = input(f'A continuacion se generara un contrasaña numerica\nPor custiones de seguridad se agregaran simbolos\n¿Estas deacuerdo? Y/N\n')
        if opsA1 in ['y', 'Y']:
            opsA2 = input(f'¿Esta seguro? (El tamaño de la contraseña cambiará) Y/N\n')
            if opsA2 in ['y', 'Y']:
                print('Ok, espere un momento...')
                time.sleep(5)
                os.system('cls')
                contrasenia = Generar_contra_Num_Simbo(tamanio)
                break
            elif opsA2 in ['n', 'N']:
                print('Regresando...')
                time.sleep(3)
                os.system('cls')
                return seguridad(tamanio)
            else:
                print(f'Opscion no encontrada\nIntente de nuevo.')
                time.sleep(1)
                os.system('cls')
        elif opsA1 in ['n', 'N']:
            opsA3 = input(f'¿Esta seguro? Y/N\n')
            if opsA3 in ['y', 'Y']:
                opsA4 = input(f'Por custiones de seguridad se recomienda simbolos.\n¿Sigue seguro? Y/N\n')
                if opsA4 in ['y', 'Y']:
                    print('Ok, espere un momento...')
                    time.sleep(5)
                    os.system('cls')
                    contrasenia = Generar_contra_Num(tamanio)
                    break
                elif opsA4 in ['n', 'N']:
                    print('Regresando...')
                    time.sleep(3)
                    os.system('cls')
                    return seguridad(tamanio)
                else:
                    print(f'Opción no encontrada\nIntente de nuevo.')
                    time.sleep(1)
                    os.system('cls')
            elif opsA3 in ['n', 'N']:
                print('Regresando...')
                time.sleep(3)
                os.system('cls')
                return seguridad(tamanio)
            
            else:
                print(f'Opcioón no encontrada\nIntente de nuevo.')
                time.sleep(1)
                os.system('cls')
        else:
            print(f'Opción no encontrada\nIntente de nuevo.')
            time.sleep(1)
            os.system('cls')   
    funcion = 1
    z = 0
    impresionContrasenia(contrasenia, tipado, funcion)
    return contrasenia, tipado, funcion

def Generar_contra_Num(largePass):
    y = ''
    x = int()
    Pass = []
    time.sleep(4)
    for i in range(largePass):
        x = random.choice(numeros)
        Pass.append(x)
    y = ''.join(Pass)
    return y

def Generar_contra_Num_Simbo(largePass):
    z = ''
    x = int()
    y = str()
    Pass = []
    for i in range(largePass - largePass // 2):
        x = random.choice(numeros)
        Pass.append(x)
        y = random.choice(signos)
        Pass.append(y)

    z = ''.join(Pass)
    return z

def contraseniaAlfabetica(metodo, tamanio):
    elementos = []
    elementosIniciales = ["¿"]
    elemento = str()
    contrasenia = ""
    tipado = "alf"
    global funcion
    
    os.system("cls")
    if metodo == 'a':
        funcion = 2
        os.system("cls")
        time.sleep(0.5)
        print("\n-------- LLENADO MANUAL - CONTRASEÑA ALFABÉTICA --------\n\n")
        for i in range(tamanio):
            validar = False
            while validar == False:
                c = 0
                time.sleep(0.4)
                elemento = input(f"-Ingrese un posible elemento para la contraseña (ingresado No.{i + 1}):")
                for j in letrasMin:
                    if elemento == j:
                        c = 1
                for j in letrasMay:
                    if elemento == j:
                        c = 1
                if len(elemento) == 1:
                    for k in elementosIniciales:
                        if elemento == k:
                            print("\n--> La letra ya fue ingresada. Intente de nuevo.\n")
                            validar = False
                            break
                        elif c == 0:
                            print("\n--> No se ingresó una letra. Intente de nuevo.\n")
                            validar = False
                            break
                        else:
                            validar = True
                    if validar == True:
                        elementosIniciales.append(elemento)
                else:
                    print("\n--> Debe ingresar una sola letra (mayúscula o minúscula). Intente de nuevo.\n")
            if i == 0:
                elementosIniciales.pop(0)
        
        time.sleep(0.5)
        print("\nProcesando ...")
        time.sleep(2)
        os.system ("cls")
        print("\nGenerando contraseña. Espere un momento por favor ...")
        time.sleep(5)
        os.system("cls")
        for i in range(tamanio):
            indice = random.randint(0, (tamanio - 1))
            elemento = elementosIniciales[indice]
            for j in elementos:
                if j == elemento:
                    indice = random.randint(0, (tamanio - 1))
                    elemento = elementosIniciales[indice]
                    break
            elementos.append(elemento)
    else:
        funcion = 2
        for i in range(tamanio):
            vector = random.randint(1, 2)
            indice = random.randint(0, 26)
            if vector == 1:
                elementos.append(letrasMin[indice])
            else:
                elementos.append(letrasMay[indice])
                  
    contrasenia = "".join(elementos)
    z = 0
    funcion = 2
    impresionContrasenia(contrasenia, tipado, funcion)
    return contrasenia, tipado, funcion

def contraseniaAlfanumerica(metodo, tamanio):
    alfanum=["¿"]
    elementos = []
    contrasenia = ""
    tipado = 'alfnum'
    global funcion
    global z
    
    if metodo == 'a':
        time.sleep(0.5)
        os.system("cls")
        time.sleep(0.5)
        print("\n-------- LLENADO MANUAL - CONTRASEÑA ALFANUMÉRICA --------\n\n")
        for a in range(tamanio):
            validar = False
            while validar == False:
                time.sleep(0.4)
                caracter=input(f'Inserta el caracter No.{a+1} por favor\n-->')
                if len(caracter) > 1:
                    validar = False
                    print('Haz insertado mas de 2 caracteres, por favor intentalo de nuevo\n')
                elif caracter == " ":
                    validar = False
                    print('Haz insertado mas de 2 caracteres, por favor intentalo de nuevo\n')
                else:
                    for k in alfanum:
                        if caracter == k:
                            print("\n--> El caracter ya fue ingresado. Intente de nuevo.\n")
                            validar = False
                        else:
                            validar = True
            alfanum.append(caracter)
            if a == 0:
                alfanum.pop(0)
                
        time.sleep(0.5)
        print("\nProcesando ...")
        time.sleep(2)
        os.system ("cls")
        print("\nGenerando contraseña. Espere un momento por favor ...")
        time.sleep(5)
        os.system("cls")
        for i in range(tamanio):
            indice = random.randint(0, (tamanio - 1))
            elemento = alfanum[indice]
            for j in elementos:
                if j == elemento:
                    indice = random.randint(0, (tamanio - 1))
                    elemento = alfanum[indice]
                    break
            elementos.append(elemento)
        alfanum = elementos
    else:
        alfanum.pop(0)
        for a in range(tamanio):
            Caracter=random.choice(caracteres)
            caracteeer=random.choice(Caracter)
            alfanum.append(caracteeer)
            if caracteeer==alfanum[a-1]:
                alfanum[a-1]=random.choice(Caracter)
                
    contrasenia = "".join(alfanum)
    z = 0
    funcion = 3
    impresionContrasenia(contrasenia, tipado, funcion)
    return contrasenia, tipado, funcion

def impresionContrasenia(contrasenia, tipado, funcion):
    os.system("cls")
    global z
    tamanio = len(contrasenia)
    
    print("\n-------- IMPRESIÓN DE RESULTADOS - CONTRASEÑA ", end = "")
    if funcion == 1:
        print("NUMÉRICA --------")    
    elif funcion == 2:
        print("ALFABÉTICA --------")
    else:
        print("ALFANUMÉRICA --------")
    
    time.sleep(1.2)
    if z == 0:
        print(f"\n-- Proceso finalizado con éxito --\n-- Contraseña generada: {contrasenia} --\n-- Tamaño de la contraseña: {tamanio} elementos --")
    else:
        print(f"\n-- Cambios realizados con éxito --\n-- Nueva contraseña: {contrasenia} --\n-- Tamaño de la contraseña: {tamanio} elementos --")

def validarModificacion():
    a = 1
    while True:
        if a == 1:
            time.sleep(1)
        else:
            time.sleep(0.45)
        opcion = input("\n-¿Desea modificar alguna parte de la contraseña (S/N)?")
        opcion = opcion.upper()
        if opcion == 'S' or opcion == 'N':
            break
        elif a == 4:
            print("\n--> Solo tiene un intento más. De lo contrario, el programa dejará de ejecutarse por defecto. Vuelva a intentarlo.")
            a += 1
        elif a == 5:
            opcion = 'e'
            break
        else:
            print("\n--> Opción seleccionada no encontrada. Intente de nuevo.")
            a += 1
    
    return opcion

def opcionesModificacion():
    opcion = str()
    print("\n\n------- OPCIONES DE MODIFICACIÓN -------\n\na) Reemplazar un elemento\nb) Reemplazar entre un rango\nc) Reemplazar toda la contraseña")
    b = 1
    while True:
        time.sleep(1.2)
        opcion = input("\n-Seleccione alguna opción:")
        opcion = opcion.lower()
        if opcion == 'a' or opcion == 'b' or opcion == 'c':
            break
        elif b == 4:
            print("\n--> Solo tiene un intento más. De lo contrario, el programa dejará de ejecutarse por defecto. Vuelva a intentarlo.")
            b += 1
        elif b == 5:
            opcion = 'e'
            break
        else:
            print("\n--> Opción seleccionada no encontrada. Intente de nuevo.")
            b += 1
    
    return opcion

def guardarContrasenias(contrasenia):
    global usuario
    motivo = opcion = str()
    elementos = dict()
    elementoGuardar = dict()
    
    os.system("cls")
    time.sleep(0.45)
    print("\n\t\t--------- GUARDADO DE LA CONTRASEÑA ---------\n\nSi desea, puede especificar hacia qué va dirigida la contraseña:\n\na) Cuenta de Google" + 
          "\t\tb) Cuenta de Instagram\t\tc) Cuenta de Facebook\nd) Cuenta de Twitter\t\te) Cuenta de Discord" + "\t\tf) Cuenta de Tik Tok" + 
          "\ng) Cuenta de Linkdin\t\th) Correo de Microsoft\t\ti) Especificar\nj) No especificar")
    
    while True:
        time.sleep(0.45)
        opcion = input("\n-Seleccione una opción:")
        opcion = opcion.lower()
        if opcion == 'a' or opcion == 'b' or opcion == 'c' or opcion == 'd' or opcion == 'e' or opcion == 'f' or opcion == 'g' or opcion == 'h' or opcion == 'i' or opcion == 'j':
            break
        else:
            print("\n--> Opción seleccionada no encontrada. Intente de nuevo.")
            
    if opcion == 'a':
        motivo = "Cuenta de Google"
    elif opcion == 'b':
        motivo = "Cuenta de Instagram"
    elif opcion == 'c':
        motivo = "Cuenta de Facebook"
    elif opcion == 'd':
        motivo = "Cuenta de Twitter"
    elif opcion == 'e':
        motivo = "Cuenta de Discord"
    elif opcion == 'f':
        motivo = "Cuenta de Tik Tok"
    elif opcion == 'g':
        motivo = "Cuenta de Linkdin"
    elif opcion == 'h':
        motivo = "Correo de Microsoft"
    elif opcion == 'i':
        time.sleep(0.45)
        motivo = input("-Especifique el motivo de la contraseña:")
    else:
        motivo = "No especificado"
    
    time.sleep(0.45)
    print("\n\nProcesando ...")
    time.sleep(3)
    os.system("cls")
    print("\nGuardando contraseña. Espere un momento por favor ...")
    elementos = historialDB[usuario]
    elementoGuardar = {contrasenia : motivo}
    elementos.update(elementoGuardar)
    historialDB[usuario] = elementos
    time.sleep(4.25)
    os.system("cls")
    time.sleep(0.45)
    print("\n--------- GUARDADO DE LA CONTRASEÑA ---------\n\nContraseña guardada correctamente")
    time.sleep(3)

def modificarContrasenia(contrasenia, tipado, funcion, opcion):
    global z
    continuar = False
    tamanio = len(contrasenia)
            
    if opcion == 'a':
        posicion = int()
        while True:
            try:
                while True:
                    time.sleep(0.55)
                    posicion = int(input("\n-Indique la posición en donde se encuentra el elemento a reemplazar:"))
                    posicion -= 1
                    if posicion >= 0 and posicion <= (tamanio - 1):
                        continuar = True
                    else:
                        continuar = False
                        print("\n--> Posición indicada fuera del rango de la contraseña. Intente de nuevo.")
                    if continuar == True:
                        elementoR = str()
                        time.sleep(0.4)
                        elementoR = input("-Ingrese el nuevo elemento:")
                        if len(elementoR) == 1:
                            if elementoR == " " or elementoR == "":
                                print("\n--> La contraseña no puede contener espacios vacíos. Intente de nuevo.")
                            elif tipado == "num":
                                if str.isdigit(elementoR) == True:
                                    break
                                else:
                                    print("\n--> Debe ingresar un número. Intente de nuevo.")
                            elif tipado == "alf":
                                if str.isalpha(elementoR) == True:
                                    break
                                else:
                                    print("\n--> Debe ingresar una letra (mayúscula o minúscula). Intente de nuevo.")
                            else:
                                break
                        else:
                            print("\n--> Solo debe ingresar un elemento. Intente de nuevo.")
                break
            except ValueError:
                print("\n--> Tipo de dato ingresado no válido. Intente de nuevo")
        arreglo = list(contrasenia)
        arreglo[posicion] = elementoR
    elif opcion == 'b':
        xI = xF = int()
        c = 0
        control = False
        valido = False
        pase = False
        
        while True:
            try:
                while True:
                    time.sleep(0.4)
                    xI = int(input("\n-Ingresa la posición inicial:"))
                    if xI >= 1 and xI <= (tamanio - 1):
                        control = True
                    else:
                        if xI == tamanio:
                            control = False
                            print("\n--> El rango no puede establecerse al final de la contraseña. Intente de nuevo.")
                        else:
                            control = False
                            print("\n--> Posición indicada fuera del rango de la contraseña. Intente de nuevo.")
                    if control == True:
                        time.sleep(0.4)
                        xF = int(input("-Ingresa la posición final:"))
                        if xF > xI and xF <= tamanio:
                            break
                        else:
                            if xF == xI:
                                control = False
                                print("\n--> La posición final no puede ser igual a la inicial. Intente de nuevo.")
                            elif xF < xI:
                                print("\n--> La posición final no puede ser menor a la inicial. Intente de nuevo.")
                            else:
                                control = False
                                print("\n--> Posición indicada fuera del rango de la contraseña. Intente de nuevo.")
                break
            except ValueError:
                print("\n--> Tipo de dato ingresado no válido. Intente de nuevo.")
                
        while valido == False:
            elementos = str()
            time.sleep(0.4)
            elementos = input("\n-Ingresa los nuevos elementos:")
            if len(elementos) == ((xF - xI) + 1):
                pase = True
            else:
                print("\n--> El No. de elementos ingresados no coincide con el límite marcado. Intente de nuevo.")
                pase = False
            
            if pase == True:
                if tipado == "num":
                    if str.isdigit(elementos):
                        break
                    else:
                        print("\n--> Debe ingresar solo números. Intente de nuevo.")
                elif tipado == 'alf':
                    almaceaje = list(elementos)
                    for i in almaceaje:
                        if str.isalpha(i) == False:
                            print("\n--> Solo puede ingresar letras ((mayúsculas o minúsculas). Intente de nuevo.\n")
                            valido = False
                            break
                        else:
                            valido = True
                else:
                    break
        arreglo = list(contrasenia)
        arreglo2 = list(elementos)
        for j in range(xI, (xF + 1)):
            arreglo[j - 1] = arreglo2[c]
            c += 1
    
    time.sleep(0.5)
    print("\n\nProcesando ...")
    time.sleep(1.5)
    os.system("cls")
    print("\nRealizando la modificación. Espere un momento por favor ...")
    time.sleep(4.5)
    contrasenia = ""
    contrasenia = "".join(arreglo)
    z = 1
    impresionContrasenia(contrasenia, tipado, funcion)
    return contrasenia

def imprimirContrasenias():
    global usuario
    contrasenias = dict()
    valores = []
    contrasenias = historialDB[usuario]
    
    if contrasenias:
        time.sleep(0.5)
        print(f"\n--------- PANEL - CONTRASEÑAS GUARDADAS ---------\n\n--- Usuario: {usuario} ---\n")
        time.sleep(0.5)
        print("\nContraseña\t\tAsociación\n")
        
        for i in contrasenias.values():
            valores.append(i)
        c = 0
        for clave in contrasenias.keys():
            time.sleep(0.4)
            if len(clave) == 16:
                print(clave, end = "\t")
            else:
                print(clave, end = "\t\t")
            for j in range(1):
                print(valores[c], end = "")
                c += 1
            print()
    else:
        time.sleep(0.55)
        print("--> Su cuenta no tiene contraseñas guardadas")
        
    time.sleep(2.5)
    input("\n\nPresione ENTER para regresar al menú")
    print("Regresando al menú. Espere un momento ...")
    time.sleep(4)

def eliminarContrasenias():
    global usuario
    contrasenias = dict()
    contraseniasE = []
    contrasenia = opcion = str()
    validar = False
    b = 1
    c = 1
    
    contrasenias = historialDB[usuario]
    time.sleep(0.55)
    print("\n--------- ELIMINACIÓN DE CONTRASEÑAS ---------\n")
    if contrasenias:
        for clave in contrasenias.keys():
            contraseniasE.append(clave)
        while True:
            time.sleep(0.5)
            contrasenia = input("-Ingrese la contraseña que desea eliminar:")
            validar = False
            for i in contraseniasE:
                if contrasenia == i:
                    validar = True
                    break
                else:
                    validar = False
            if validar == True:
                while True:
                    time.sleep(0.5)
                    opcion = input(f"-¿Está segur@ de eliminar esta contraseña [{contrasenia}] (S/N)?")
                    opcion = opcion.upper()
                    if opcion == 'S' or opcion == 'N':
                        break
                    elif c == 4:
                        print("\n--> Solo tiene un intento más. De lo contrario, la operación se detendrá. Vuelva a intentarlo.\n")
                        c += 1
                    elif c == 5:
                        opcion = 'N'
                        break
                    else:
                        print("\n--> Opción ingresada no válida. Intente de nuevo.\n")
                        c += 1
                        
                if opcion == 'S':
                    time.sleep(1)
                    os.system("cls")
                    time.sleep(0.55)
                    print("\nEliminando contraseña ...")
                    del contrasenias[contrasenia]
                    historialDB[usuario] = contrasenias
                    time.sleep(4)
                    print("Contraseña eliminada exitosamente")
                    break
                else:
                    time.sleep(0.5)
                    print("\n\nCancelando operación ...")
                    break
            elif b == 4:
                print("\n--> Solo tiene un intento más. De lo contrario, la operación se detendrá. Vuelva a intentarlo.\n")
                b += 1
            elif b == 5:
                time.sleep(0.5)
                print("\n\nCancelando operación ...")
                break
            else:
                print("\n--> La contraseña ingresada no existe dentro de su cuenta. Vuelva a intentarlo.\n")
                b += 1
    else:
        print("\n-- Esta cuenta no contiene alguna contraseña --")
    
    time.sleep(2.5)
    input("\n\nPresione ENTER para regresar al menú")
    print("Regresando al menú. Espere un momento ...")
    time.sleep(4)
            
def menu(funcion):
    datosRetorno = []
    opcion = metodo = validacion = decision = guardado = str()
    nuevaContrasenia = ""
    contraseniaFinal = ""
    tamanio = int()
    error = False
    global control
    c = 1
    d = 1
    
    os.system ("cls")
    if control == False:
        print("\n------------ GENERADOR DE CONTRASEÑAS - MENÚ PRINCIPAL ------------\n\n1. Contraseña numérica\n2. Contraseña alfabética\n" +
              "3. Contraseña alfanumérica\n4. Consultar contraseñas guardadas\n5. Eliminar contraseña\n6. Salir")
        while True:
            try:
                while True:
                    time.sleep(1.2)
                    opcion = int(input("\n-Seleccione alguna opción del menú:"))
                    if opcion >= 1 and opcion <= 6:
                        break
                    elif c == 4:
                        print("\n--> Solo tiene un intento más. De lo contrario, el programa dejará de ejecutarse por defecto. Vuelva a intentarlo.")
                        c += 1
                    elif c == 5:
                        opcion = 0
                        break
                    else:
                        print("\n--> Opción seleccionada no detectada. Intente de nuevo.")
                        c += 1
                break
            except ValueError:
                if c == 4:
                    print("\n--> Solo tiene un intento más. De lo contrario, el programa dejará de ejecutarse por defecto. Vuelva a intentarlo.")
                    c += 1
                elif c == 5:
                    opcion = 0
                    break
                else:
                    print("\n--> Tipo de dato ingresado no válido. Intente de nuevo.")
                    c += 1
    else:
        opcion = funcion
                
    if opcion != 0 and not(opcion >= 4 and opcion <= 6):
        time.sleep(0.5)
        print("\n\nProcesando ...")
        time.sleep(3)
        os.system("cls")
        if opcion != 1:
            metodo = metodoRellenado()
        else:
            metodo = 'b'
            print("\nAsignando llenado de contraseña automático ...")
            time.sleep(0.5)
        if metodo != 'e':
            time.sleep(0.5)
            print("\nProcesando ...")
            time.sleep(3)
            os.system("cls")
            tamanio = tamanioCifrado()
            if tamanio != 0:
                if metodo == 'b':
                    time.sleep(0.5)
                    print("\nProcesando ...")
                    time.sleep(2)
                    os.system ("cls")
                    print("\nGenerando contraseña. Espere un momento por favor ...")
                    time.sleep(5)
                    os.system("cls")
                else:
                    time.sleep(0.5)
                    print("\n\nProcesando ...")
                    time.sleep(3)
                if opcion == 1:
                    datosRetorno = seguridad(tamanio)
                elif opcion == 2:
                    datosRetorno = contraseniaAlfabetica(metodo, tamanio)
                elif opcion == 3:
                    datosRetorno = contraseniaAlfanumerica(metodo, tamanio)
                control = True
                contraseniaFinal = datosRetorno[0]
                while control == True:
                    validacion = validarModificacion()
                    if validacion == 'S':
                        time.sleep(0.45)
                        print("\n\nProcesando ...")
                        time.sleep(2.5)
                        decision = opcionesModificacion()
                        if decision == 'c':
                            control = True
                            funcion = datosRetorno[2]
                            time.sleep(0.5)
                            print("\nEliminando contraseña ...")
                            time.sleep(2.5)
                            print("Reiniciando operaciones. Espere un momento ...")
                            time.sleep(3.5)
                            return menu(funcion)
                        else:
                            if decision != 'e':
                                control = True
                                if d == 1:
                                    nuevaContrasenia = modificarContrasenia(datosRetorno[0], datosRetorno[1], datosRetorno[2], decision)
                                    contraseniaFinal = nuevaContrasenia
                                    d += 1
                                else:
                                    nuevaContrasenia = modificarContrasenia(nuevaContrasenia, datosRetorno[1], datosRetorno[2], decision)
                                    contraseniaFinal = nuevaContrasenia
                                    d += 1
                            else:
                                control = False
                                time.sleep(0.5)
                                print("\n\nCancelando operación ...")
                                time.sleep(3.2)
                                return menu(funcion)
                    else:
                        time.sleep(0.5)
                        while True:
                            guardado = input("-¿Desea guardar la contraseña generada (S/N)?")
                            guardado = guardado.upper()
                            if guardado == 'S' or guardado == 'N':
                                break
                            else:
                                print("\n--> Opción ingresada no válida. Intente de nuevo")
                        
                        if guardado == 'S':
                            time.sleep(0.5)
                            print("\n\nProcesando ...")
                            time.sleep(3)
                            guardarContrasenias(contraseniaFinal)
                        control = False
                        time.sleep(0.5)
                        print("\n\nRegresando al menú. Espere un momento por favor ...")
                        time.sleep(3)
                        return menu(funcion)
                error = False
            else:
                time.sleep(0.5)
                print("\n\nCancelando operación ...")
                time.sleep(3.2)
                return menu(funcion)
        else:
            time.sleep(0.5)
            print("\n\nCancelando operación ...")
            time.sleep(3.2)
            return menu(funcion)
    else:
        if opcion == 0:
            error = True
        elif opcion == 4:
            time.sleep(0.45)
            print("\n\nProcesando ...")
            time.sleep(3)
            os.system("cls")
            imprimirContrasenias()
            return menu(funcion)
        elif opcion == 5:
            time.sleep(0.45)
            print("\n\nProcesando ...")
            time.sleep(3)
            os.system("cls")
            eliminarContrasenias()
            return menu(funcion)
        else:
            error = False
        
    return error
    
datosUsuario = []
error = None

os.system("cls")
bienvenida()
datosUsuario = iniciarSesion()
time.sleep(2)

usuario = datosUsuario[0]
if usuario != 'e' or datosUsuario[1] != 'e':
    error = menu(funcion)
    if error == True:
        time.sleep(1)
        finalizacion()
    else:
        time.sleep(1)
        despedida()
else:
    time.sleep(1)
    finalizacion()