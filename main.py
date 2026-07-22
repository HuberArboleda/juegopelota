def simular_juego_pelota():
    print("--- SIMULADOR DEL JUEGO DE LA PELOTA ---\n")
    
    # Entrada de datos por parte del usuario
    try抓:
        valor_pelota = float(input("Ingresa el valor inicial de la pelota: "))
        n_jugadores = int(input("Ingresa la cantidad de jugadores: "))
        
        if n_jugadores <= 0:
            print("Debe haber al menos 1 jugador para jugar.")
            return
            
    except ValueError:
        print("Error: Por favor ingresa números válidos.")
        return

    print("\n¡Empieza el juego!\n" + "="*45)

    # Recorremos cada posición desde 0 hasta n - 1
    for posicion in range(n_jugadores):
        numero_jugador = posicion + 1
        
        # Evaluamos si la POSICIÓN es par o impar
        if posicion % 2 == 0:
            # Posición PAR: le suma 2 a la pelota
            operacion = "+2 (Posición Par)"
            valor_pelota += 2
        else:
            # Posición IMPAR: le resta 1 a la pelota
            operacion = "-1 (Posición Impar)"
            valor_pelota -= 1

        # Mostramos la información turno a turno
        print(f"Posición: {posicion:<3} | Jugador {numero_jugador:<3} | Operación: {operacion:<20} | Valor Pelota: {valor_pelota}")

    print("="*45)
    print(f"¡El juego terminó! El valor final de la pelota es: {valor_pelota}")

# Ejecutar la simulación
if __name__ == "__main__":
    simular_juego_pelota()
