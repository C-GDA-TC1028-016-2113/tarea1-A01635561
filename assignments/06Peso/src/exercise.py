def main():
    #escribe tu código abajo de esta línea
    
    num1 = float(input("Dame el peso inicial: "))
    num2 = float(input("Dame el peso final: "))
    num3 = int(input("Dame la cantidad de meses: "))
    primera_resta = num1 - num2
    resultado = primera_resta / num3
    print("Lo que debes bajar por mes es:", resultado)


if __name__ == '__main__':
    main()
