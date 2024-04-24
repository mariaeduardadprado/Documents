saldo = 2000
saque = 2000

status = 'sucesso' if saldo >= saque else 'falha'

print(f'{status} ao realizar o saque!')