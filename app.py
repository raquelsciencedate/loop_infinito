while True:
    try: #tratamento de exceção
        #declaração de variaveis
        nome = input("informe o nome: ")  
        idade = int(input("informe a idade: "))

    #ternário
        saida = "é maior de idade." if idade >= 18 else "é menor de idade."
    #saida de dados
        print(f"{nome} {saida}")  
        continuar = input("deseja continuar? 'sim' para continuar ou outro valor para encerrar. ")
        if continuar == "sim":
            continue
        else:
            break
    except Exception as e:
        print(f"não foi possivel verificar a maioride. {e}.")
    finally:
        print("programa finalizado.")



