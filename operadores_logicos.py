#na condição "AND" para ser True, tudo tem que ser True
#na condição "OR" para ser True, apenas um tem que ser True


print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)

print(saldo >= saque or saque <= limite)

print(not saldo >= saque)