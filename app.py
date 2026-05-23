import os 

restaurantes = [ {"nome": "Taco Bell", "Categoria": "Mexicana", "Ativado": True},    
                 {"nome" : "Pandas", "Categoria": "Japonesa", "Ativado": False  }                
]


def main():
    os.system('cls' if os.name == 'nt' else 'clear') 
    exibir_nome_programa()
    exibir_opcoes() 
    escolher_opcao() 

def subtitulo(texto): 
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = "-" * (len(texto))

    print(linha)
    print (texto) 
    print(linha)

    print()


def voltar_ao_menu():
    input("Digite qualquer tecla para voltar ao menu principal. ")
    main()

def encerrar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Finalizando o app \n") 

def opcao_invalida():
    print("Opção invalida! \n")
    voltar_ao_menu()


def listar_restaurantes():
    os.system('cls' if os.name == 'nt' else 'clear')
    subtitulo("Restaurantes disponíveis: ")
    
    cont = 1
    print(f'{'Nome do restaurante:'.ljust(23)}  {'Categoria:'.ljust(22)}  Status:') 
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"] 
        categoria = restaurante ["Categoria"]
        ativado = "Ativado" if restaurante["Ativado"] else "Desativado" 
        print (f"{cont}. {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativado.ljust(20)}") 
        cont +=1 
        
    voltar_ao_menu()

def alternar_estado_restaurante():
    os.system('cls' if os.name == 'nt' else 'clear') 

    subtitulo("Alternando estado dos restaurantes")
    nome_restaurante = input("Qual restaurante você deseja alterar o estado?")
    restaurante_encontrado = False

    for restaurante in restaurantes: 

        if nome_restaurante.lower() == restaurante["nome"].lower():
            restaurante_encontrado = True
            restaurante ["Ativado"] = not restaurante ["Ativado"] 
            mensagem = f"O {nome_restaurante} foi ativado com sucesso" if restaurante ["Ativado"] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f"O {nome_restaurante} não foi encontrado")

    voltar_ao_menu() 


     
def exibir_nome_programa():
    print("Sabor express \n")  

def cadastrar_restaurante():
     os.system('cls' if os.name == 'nt' else 'clear')
     subtitulo("Cadastro de restaurante")
     nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: \n") 
     categoria = input(f"Digite a categoria do {nome_restaurante}:")

     dados_do_restaurante = {"nome": nome_restaurante, "Categoria": categoria, "Ativado": False}

     restaurantes.append(dados_do_restaurante) 

     print(f"O restaurante {nome_restaurante} foi cadastrado \n")
     decisao_novo_restaurante = str(input(f"Deseja cadastrar de novo um restaurante?  \n ".lower()))

     if decisao_novo_restaurante == "sim":
          cadastrar_restaurante()
     else:
        voltar_ao_menu()


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Mudar status do restaurante")
    print("4. Sair \n")

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha um opção:"))
        
        if opcao_escolhida == 1:
            cadastrar_restaurante() 

        elif opcao_escolhida == 2:
            listar_restaurantes() 

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            encerrar()

        else: 
            opcao_invalida()
    except ValueError: # só entra quando é erro de valor da variavel, ou seja, se o cliente digitar algo que não seja número
        opcao_invalida() 
    
    except Exception as e: # pega qualquer erro q não seja de valor, guarda ele na variavel e exibe no terminal
        print(f"Erro inesperado no código: {e}")
    
    # se houver algum erro logico , irá aparecer no terminal e não vai cair no except de cima,
    # onde qualquer erro no código estava aparecendo no terminal "opção invalida ao invés de
    # erro no terminal. Dificultando acahr aonde o erro estava. 


if __name__ == "__main__": 
    main()

