#Juego basico de 5 intentos para adivinar el numero
#Paso 1
import random

numero_secreto = random.randint(1, 10)
intentos = 0
max_intentos = 5
print("Adivina el número entre 1 y 10. ¡Tienes 5 intentos!")
while intentos < max_intentos:
    invitado = int(input("Tu número: "))
    intentos += 1
    if invitado == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
        break
    elif invitado < numero_secreto:
        print("Demasiado bajo.")
    elif abs(invitado - numero_secreto) == 1:#PASO 3
        print("¡Casi lo logras! Estás muy cerca.")
    else:
        print("Demasiado alto.")
    if invitado != numero_secreto:
        print(f"Game Over. El número era {numero_secreto}.")
    if invitado== -1: #Paso 2 Modo trampa activado
             print(f"Modo trampa activado: el número secreto es {numero_secreto}")
             intentos -= 1 # Anulamos el intento
             continue
    
while True:
    import random

    numero_secreto = random.randint(1, 10)
    intentos = 0
    max_intentos = 5
    print("Adivina el número entre 1 y 10. ¡Tienes 5 intentos!")
    while intentos < max_intentos:
        invitado = int(input("Tu número: "))
        intentos += 1
        if invitado == numero_secreto:
            print("¡Correcto! Has adivinado el número.")
            break
        elif invitado < numero_secreto:
            print("Demasiado bajo.")
        elif abs(invitado - numero_secreto) == 1:#PASO 3
            print("¡Casi lo logras! Estás muy cerca.")
        else:
            print("Demasiado alto.")
        if invitado != numero_secreto:
            print(f"Game Over. El número era {numero_secreto}.")
        if invitado== -1: #Paso 2 Modo trampa activado
                print(f"Modo trampa activado: el número secreto es {numero_secreto}")
                intentos -= 1 # Anulamos el intento
                continue
    jugar_otra_vez = input("¿Quieres jugar de nuevo? (s/n): ").lower()
   
    if jugar_otra_vez == 's':
        numero_secreto = random.randint(1, 10)
        intentos = 0
        print("¡Nuevo juego iniciado!")
        continue
    else:
        print("¡Gracias por jugar!")
                
    break