import csv


def menu():
    print("Bem-vindo ao formulário de pesquisa!")
    print("Escolha uma opção:")
    print("1 - Realizar pesquisa")
    print("2 - Sair do programa")
    opcao = input("Opção: ")
    return opcao

def realizar_pesquisa():
    email = input("Digite seu email: ")
    marca = input("Qual marca você gosta mais? ")
    cor = input("Qual sua cor preferida? ")
    valor = input("Qual a faixa de valor? ")
    carro = input("Descreva o carro ideal para você: ")
    salvar_pesquisa(email, marca, cor, valor, carro)

def salvar_pesquisa(email, marca, cor, valor, carro):
    with open('pesquisas.csv', 'a', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow([email, marca, cor, valor, carro])
    print("Pesquisa salva com sucesso!")

while True:
    opcao = menu()
    if opcao == "1":
        realizar_pesquisa()
    elif opcao == "2":
        break
    else:
        print("Opção inválida. Tente novamente.")
