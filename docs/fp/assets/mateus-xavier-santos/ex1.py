# 10/10/2024 
# Aluno: Mateus Xavier

acumulador = 0

print(
    '''
    1 - Pizza Margherita - R$ 25
    2 - Pizza Calabresa - R$ 30
    3 - Pizza Quatro Queijos - R$ 35
    4 - Encerrar Pedido (finaliza o pedido)
    '''
)

while True: 
    opcao = int(input("Informe o código do item que deseja comprar: "))
    match(opcao):
        case 1: 
            qtd = int(input("Informe a quantidade de pizzas: "))
            acumulador += 25 * qtd 
        case 2: 
            qtd = int(input("Informe a quantidade de pizzas: "))
            acumulador += 30 * qtd 
        case 3: 
            qtd = int(input("Informe a quantidade de pizzas: "))
            acumulador += 35 * qtd 
        case 4: 
            break
        case _: 
            print("Código inválido, tente novamente") 

print("Total:", acumulador, "R$")
print("Agradecemos seu pedido, boa refeição!")
