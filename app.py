import random

produtos = {
    "Mortal Kombat": {"preço": 350.00, "estoque": 100},
    "Blasphemous": {"preço": 29.99, "estoque": 150},
    "The last of us": {"preço": 39.00, "estoque": 50},
}

total_vendas = 0.20

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o preço de {nome}: "))
    estoque = int(input(f"Digite a quantidade dos jogos em estoque de {nome}: "))
    produtos[nome] = {"preço": preco, "estoque": estoque}
    print(f"Produto/jogo cadastrado com sucesso!\n")

def exibir_produtos():
    print("Produtos disponíveis: ")
    for produto, info in produtos.items():
        print(f"{produto} - Preço: R${info['preço']:.2f}, Estoque: {info['estoque']} unidades")
    print()

def realizar_venda():
    global total_vendas  # Declara que total_vendas é a variável global
    produto_vendido = input("Digite o nome do produto/jogo que deseja comprar: ")

    if produto_vendido in produtos: 
        quantidade = int(input(f"Digite a quantidade de {produto_vendido} que deseja comprar: "))
        if produtos[produto_vendido]["estoque"] >= quantidade:
            valor_venda = quantidade * produtos[produto_vendido]["preço"]
            produtos[produto_vendido]["estoque"] -= quantidade
            total_vendas += valor_venda  # Agora a atualização será feita corretamente
            print(f"Venda realizada: {quantidade}x {produto_vendido} - Total: R${valor_venda:.2f}\n")
        else:
            print("Quantidade em estoque insuficiente.\n")
    else: 
        print("Produto não encontrado.\n")

def exibir_vendas():
    print(f"\nTotal de vendas realizadas: R${total_vendas:.2f}\n")

def sortear_promocao():
    produto_sorteado = random.choice(list(produtos.keys()))
    desconto = random.randint(10, 50)
    produtos[produto_sorteado]["preço"] *= (1 - desconto / 100)
    print(f"\nPromoção! O produto {produto_sorteado} está com {desconto}% de desconto!\n")

def menu():
    while True: 
        print("=== Sistema de Gerenciamento de Loja de Games ===")
        print("1. Cadastrar produtos")
        print("2. Exibir produtos")
        print("3. Realizar venda")
        print("4. Exibir total de vendas")
        print("5. Sortear promoção")
        print("6. Sair")

        opcao = input("Escolha uma opção: ") 

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            exibir_produtos()
        elif opcao == "3":
            realizar_venda()
        elif opcao == "4":
            exibir_vendas()
        elif opcao == "5":
            sortear_promocao()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

menu()
