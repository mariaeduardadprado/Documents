def recomendar_plano(consumo):
    if consumo <= 10:
        return 'O plano recomendado é o Essencial Fibra - 50Mbps'
    elif consumo <= 20:
        return 'O plano recomendado é o Prata Fibra - 100Mbp'
    else:
        return 'O plano recomendado é o Premium Fibra- 300Mbps'

consumo = float(input())
print(recomendar_plano(consumo))
