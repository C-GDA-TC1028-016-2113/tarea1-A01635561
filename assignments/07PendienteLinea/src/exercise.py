def main():
    #escribe tu código abajo de esta línea
    
    num1 = float(input("Dame x1: "))
    num2 = float(input("Dame y1: "))
    num3 = float(input("Dame x2: "))
    num4 = float(input("Dame y2: "))
    pendiente_arriba = num4 - num2
    pendiete_abajo = num3 - num1
    pendiente = pendiente_arriba / pendiete_abajo
    print("Pendiente:", pendiente)



if __name__ == '__main__':
    main()
