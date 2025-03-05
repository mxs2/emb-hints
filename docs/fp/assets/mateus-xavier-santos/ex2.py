# 10/10/2024 
# Aluno: Mateus Xavier

age = int(input("Informe a idade do seu aparelho: "))

if age < 0:
    print("Tempo inválido")
elif age < 1:
    print("Seu smartphone é de última geração")
elif age >= 1 and age <= 3:
    print("Seu smartphone é atual")
elif age >= 4 and age <= 5:
    print("Seu smartphone está moderamente desatualizado")
elif age > 5:
    print("Seu smartphone está obsoleto")
