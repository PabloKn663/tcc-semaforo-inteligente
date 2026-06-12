from pathlib import Path
import joblib
import pandas as pd


PASTA_ATUAL = Path(__file__).resolve().parent
CAMINHO_MODELO = PASTA_ATUAL / "modelos" / "modelo_tempo_semaforo.pkl"


modelo = joblib.load(CAMINHO_MODELO)


cenarios = pd.DataFrame([
    {"veiculos": 4, "emergencia": 0, "hora_pico": 0},
    {"veiculos": 12, "emergencia": 0, "hora_pico": 0},
    {"veiculos": 22, "emergencia": 0, "hora_pico": 1},
    {"veiculos": 31, "emergencia": 0, "hora_pico": 1},
    {"veiculos": 10, "emergencia": 1, "hora_pico": 0},
])


previsoes = modelo.predict(cenarios)


print("=== TESTE DO MODELO DE IA ===")

for i, previsao in enumerate(previsoes):
    veiculos = cenarios.loc[i, "veiculos"]
    emergencia = cenarios.loc[i, "emergencia"]
    hora_pico = cenarios.loc[i, "hora_pico"]

    print(
        f"Cenário {i + 1}: "
        f"veículos={veiculos}, "
        f"emergência={emergencia}, "
        f"hora_pico={hora_pico} "
        f"=> tempo previsto={round(previsao)}s"
    )