MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Por favor, informe sua idade: "))

if idade >= MAIOR_IDADE:
    input("Pode tirar a CNH.")
if idade <= MAIOR_IDADE:
    input("Não pode tirar CNH. ")


if idade >= MAIOR_IDADE:
    input("Pode tirar a CNH.")
else:
    input("Ainda nao pode tirar CNH. ")


if idade >= MAIOR_IDADE:
    input("Maior de idade, pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    input("Tá quase lá, ainda nao pode tirar CNH, mas já pode fazer as aulas teoricas.")
else:
    input("Menor de idade, ainda nao pode fazer aulas teoricas e nem tirar CNH.")
          
          
