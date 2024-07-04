#Almacenar Los puntajes y datos del jugador 
puntajes = []

#Registrar los puntajes
def Registrar_Puntaje():
    id_jugador = input("Ingrese su ID: ")
    nombre = input("Ingrese su nombre: ")
    valorant = int(input("Ingrese el puntaje obtenido de VALORANT: "))
    fortnite = int(input("Ingrese el puntaje obtenido de FORTNITE: "))
    fifa = int(input("Ingrese el puntaje obtenido de FIFA: "))
    tipo = input("Ingrese el tipo de jugador (PRINCIPIANTE, AVANZADO, EXPERTO): ")
    
    # Validar los datos ingresados
    if id_jugador and nombre and tipo and (valorant >= 0) and (fortnite >= 0) and (fifa >= 0):
        puntajes.append({
            "id_jugador": id_jugador,
            "nombre": nombre,
            "valorant": valorant,
            "fortnite": fortnite,
            "fifa": fifa,
            "tipo": tipo
        })
        print("[+] Registro exitoso!!!")
    else:
        print("[ERROR] Los datos no se pudieron registrar...")
        
#Listar los Puntajes
def Listar_Puntaje():
    print("Id Jugador | Nombre | VALORANT | FORTNITE | FIFA | Tipo")
    print("-----------------------------------------------------")
    for puntaje in puntajes:
        print((f"{puntaje['id_jugador']} | {puntaje['nombre']} | {puntaje['valorant']} | {puntaje['fortnite']} | {puntaje['fifa']} | {puntaje['tipo']}")
)

#Imprimir puntaje por tipo
def Imprimir_Por_Tipo():
    tipo = input("Ingrese el tipo de jugador a imprimir (Principiante, Avanzado, Experto): ")
    with open(f"puntajes_{tipo}.txt", "w") as file:
        file.write("Id Jugador | Nombre | VALORANT | FORTNITE | FIFA | Tipo\n")
        file.write("-----------------------------------------------------\n")
        for puntaje in puntajes:
            if puntaje['tipo'].lower() == tipo.lower():
                file.write(f"{puntaje['id_jugador']} | {puntaje['nombre']} | {puntaje['valorant']} | {puntaje['fortnite']} | {puntaje['fifa']} | {puntaje['tipo']}\n")
    print(f"Puntajes del tipo {tipo} impresos en el archivo puntajes_{tipo}.txt")



def Menu_Principal():
    print("1. Registrar puntaje de torneo")
    print("2. Listar todos los puntajes")
    print("3. Imprimir por tipo")
    print("4. Salir del programa")
    
    
while True:
    Menu_Principal()
    opcion = input("Ingrese la opcion que desea realizar: ")  
    
    if opcion == "1":
        print("[+] REGISTRANDO PUNTAJE")
        Registrar_Puntaje()
    elif opcion == "2":
        Listar_Puntaje()
    elif opcion == "3":
        Imprimir_Por_Tipo()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("[ERROR] Por favor ingrese opcion valida!!!")