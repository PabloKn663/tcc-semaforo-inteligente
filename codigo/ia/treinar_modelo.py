from pathlib import Path
import pandas as pd
import joblib

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


PASTA_ATUAL = Path(__file__).resolve().parent
PASTA_DATASET = PASTA_ATUAL / "dataset"
PASTA_MODELOS = PASTA_ATUAL / "modelos"

CAMINHO_DATASET = PASTA_DATASET / "dataset_treinamento.csv"
CAMINHO_MODELO = PASTA_MODELOS / "modelo_tempo_semaforo.pkl"


def definir_tempo_ideal(veiculos, emergencia, hora_pico):
    """
    Define o tempo ideal do semáforo para criar os dados de treino.

    Nesta fase do projeto, os dados ainda são simulados porque a contagem
    real por câmera com OpenCV será integrada depois.
    """

    if emergencia == 1:
        return 45

    if veiculos <= 5:
        tempo = 10
    elif veiculos <= 15:
        tempo = 20
    elif veiculos <= 25:
        tempo = 34
    else:
        tempo = 45

    if hora_pico == 1:
        tempo += 5

    return min(tempo, 45)


def criar_dataset():
    """
    Cria um conjunto de dados com diferentes situações de trânsito.
    """

    dados = []

    for veiculos in range(0, 41):
        for emergencia in [0, 1]:
            for hora_pico in [0, 1]:
                tempo_ideal = definir_tempo_ideal(
                    veiculos=veiculos,
                    emergencia=emergencia,
                    hora_pico=hora_pico
                )

                dados.append({
                    "veiculos": veiculos,
                    "emergencia": emergencia,
                    "hora_pico": hora_pico,
                    "tempo_ideal": tempo_ideal
                })

    df = pd.DataFrame(dados)

    PASTA_DATASET.mkdir(exist_ok=True)
    df.to_csv(CAMINHO_DATASET, index=False, encoding="utf-8")

    return df


def treinar_modelo(df):
    """
    Treina uma Árvore de Decisão para prever o tempo ideal do semáforo.
    """

    entradas = df[["veiculos", "emergencia", "hora_pico"]]
    saida = df["tempo_ideal"]

    x_treino, x_teste, y_treino, y_teste = train_test_split(
        entradas,
        saida,
        test_size=0.25,
        random_state=42
    )

    modelo = DecisionTreeRegressor(
        max_depth=4,
        random_state=42
    )

    modelo.fit(x_treino, y_treino)

    previsoes = modelo.predict(x_teste)
    erro_medio = mean_absolute_error(y_teste, previsoes)

    PASTA_MODELOS.mkdir(exist_ok=True)
    joblib.dump(modelo, CAMINHO_MODELO)

    return erro_medio


def main():
    print("=== TREINAMENTO DA IA DO SEMÁFORO INTELIGENTE ===")

    dataset = criar_dataset()
    print(f"Dataset criado com {len(dataset)} registros.")
    print(f"Dataset salvo em: {CAMINHO_DATASET}")

    erro = treinar_modelo(dataset)
    print("Modelo Decision Tree treinado com sucesso.")
    print(f"Erro médio aproximado: {erro:.2f} segundos.")
    print(f"Modelo salvo em: {CAMINHO_MODELO}")


if __name__ == "__main__":
    main()