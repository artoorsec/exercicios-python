
lista = []

while True:
    
    try:
        selecionar = int(input("Selecione uma opção:\n[1] Inserir [2] Apagar [3] Listar [4] Sair\n"))
        
        if selecionar == 1:
            valor = input("insira o item desejado: ")
            lista.append(valor)
        elif selecionar == 2:
            valor = input("Insira o item que deseja remover: ")
            try:
                lista.remove(valor)
                print("Item removido")
            except ValueError:
                print("Item não encontrado")
        elif selecionar == 3:
            for i, item in enumerate(lista):
                print(i + 1, item)
        elif selecionar == 4:
            break
        
    except ValueError:
        print("Insira uma opção válida!!!")





       



