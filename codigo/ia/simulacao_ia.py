def calcular_tempo_semaforo(qtd_veiculos, emergencia=False):
    if emergencia:
        return 45

    if qtd_veiculos <= 5:
        return 10
    elif qtd_veiculos <= 15:
        return 20
    elif qtd_veiculos <= 25:
        return 34
    else:
        return 45


tempo_padrao = 20
qtd_veiculos = 18
emergencia = False

tempo_ia = calcular_tempo_semaforo(qtd_veiculos, emergencia)

print("=== SIMULAÇÃO DO SEMÁFORO INTELIGENTE ===")
print(f"Veículos detectados: {qtd_veiculos}")
print(f"Tempo padrão sem IA: {tempo_padrao} segundos")
print(f"Tempo calculado pela IA: {tempo_ia} segundos")

if tempo_ia > tempo_padrao:
    print("Decisão: aumentar tempo verde para melhorar o fluxo.")
elif tempo_ia < tempo_padrao:
    print("Decisão: reduzir tempo verde por baixo fluxo.")
else:
    print("Decisão: manter tempo padrão.")