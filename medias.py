def calcular_media(valor1, valor2, valor3):
    return(valor1 + valor2 + valor3) /3

def main():
    try:
        valor1 = float(input("Digite o primeiro valor:" ))
        valor2 = float(input("Digite o segundo valor:" ))
        valor3 = float(input("Digite o terceiro valor:" ))
        
        media = calcular_media(valor1, valor2, valor3)
        
        print("A media dos valores é:", media)
    except ValueError:
        print("Por favor, insira apeas número")
        
        if __name__ == "__main__":
            main()
