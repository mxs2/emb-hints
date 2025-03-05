# 10/10/2024 
# Aluno: Mateus Xavier

cqtd1 = cqtd2 = qtd1 = qtd2 = 0

print(
    '''
    1 - Consulta Geral
    2 - Exame Laboratorial
    3 - Fim (encerra o programa)
    '''
)

while True: 
    opcao = int(input("Informe o código do serviço que você deseja: "))
    match(opcao):
        case 1: 
            qtd1 = int(input("Informe a quantidade de atendimento necessária: "))
            cqtd1 += qtd1
        case 2: 
            qtd2 = int(input("Informe a quantidade de atendimento necessária: "))
            cqtd2 += qtd2
        case 3: 
            break
        case _: 
            print("Código inválido, tente novamente") 
        
print("Serviço 1:", cqtd1)
print("Serviço 2:", cqtd2)
print("Quantidade total de atendimentos:", cqtd1 + cqtd2)

if cqtd1 > cqtd2:
    print("Consulta Geral teve mais atendimentos") 
elif cqtd1 == cqtd2:
    print("Os serviços empataram no número de atendimento(s)")
else:
    print("Exame Laboratorial teve mais atendimentos")

print("Obrigado por utilizar nossos serviços!")
