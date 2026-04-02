tarefas = []

while True:
    print("\n1. Adicionar")
    print("2. Ver")
    print("3. Sair")
    opcao = input("opcao: ")

    if opcao == "1":
        tarefa = input("Tarefa: ")
        tarefas.append(tarefa)
        print("Adicionado!")

    elif opcao == "2":
        print(tarefas)

    elif opcao == "3":
        break