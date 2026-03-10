tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nLista de tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i} - {tarefa}")

def remover_tarefa():
    listar_tarefas()
    try:
        numero = int(input("Digite o número da tarefa para remover: "))
        tarefas.pop(numero - 1)
        print("Tarefa removida!")
    except:
        print("Número inválido.")

while True:
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida")
