conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
cheque_especial = 450
saque = 2500
cartao_credito = 1000

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque do saldo com uso do limite do cheque especial realizado com sucesso")
    else:
        print("Saldo e limites insuficientes.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Limite insuficiente")

elif conta_especial:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial + cartao_credito):
        print("Saque liberado com uso dos limites de credito e do cheque especial")
    else:
        print("Saldos e limites insuficientes no momento, pedimos desculpas pelo transtorno")


