from flask import Flask, render_template, jsonify
from datetime import datetime
from pathlib import Path
import random
import sqlite3
import joblib
import pandas as pd


app = Flask(__name__)


# Caminho principal do projeto
PASTA_PROJETO = Path(__file__).resolve().parents[2]

# Caminho do banco de dados local
PASTA_BANCO = PASTA_PROJETO / "banco_de_dados"
CAMINHO_BANCO = PASTA_BANCO / "semaforo_inteligente.db"

# Caminho do modelo de IA treinado
CAMINHO_MODELO_IA = (
    PASTA_PROJETO
    / "codigo"
    / "ia"
    / "modelos"
    / "modelo_tempo_semaforo.pkl"
)

# Controla a emergência simulada.
# Depois, essa parte será substituída pela leitura real do RFID.
ciclos_emergencia = 0


def carregar_modelo_ia():
    """
    Carrega o modelo treinado da Árvore de Decisão.

    Se o modelo ainda não existir, o sistema avisa no terminal.
    """

    if not CAMINHO_MODELO_IA.exists():
        print("Modelo de IA não encontrado.")
        print("Execute primeiro:")
        print(r".\.venv\Scripts\python.exe codigo\ia\treinar_modelo.py")
        return None

    modelo = joblib.load(CAMINHO_MODELO_IA)
    print("Modelo de IA carregado com sucesso.")
    return modelo


modelo_ia = carregar_modelo_ia()


def conectar_banco():
    return sqlite3.connect(CAMINHO_BANCO)


def criar_tabela_se_nao_existir():
    """
    Cria a tabela usada pelo dashboard.

    Nesta fase do protótipo, mantemos uma tabela simples para registrar os testes.
    A modelagem final do TCC será apresentada com DER e tabelas normalizadas.
    """

    PASTA_BANCO.mkdir(exist_ok=True)

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros_dashboard (
            id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
            cruzamento INTEGER NOT NULL,
            veiculos_detectados INTEGER NOT NULL,
            tempo_padrao INTEGER NOT NULL,
            tempo_ia INTEGER NOT NULL,
            tempo_sem_ia INTEGER NOT NULL,
            tempo_com_ia INTEGER NOT NULL,
            melhora_percentual REAL NOT NULL,
            decisao TEXT NOT NULL,
            emergencia_detectada INTEGER NOT NULL,
            status_emergencia TEXT NOT NULL,
            data_hora TEXT NOT NULL
        );
    """)

    conexao.commit()
    conexao.close()


def salvar_registro(dados):
    """
    Salva no banco as informações exibidas no dashboard.
    """

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO registros_dashboard (
            cruzamento,
            veiculos_detectados,
            tempo_padrao,
            tempo_ia,
            tempo_sem_ia,
            tempo_com_ia,
            melhora_percentual,
            decisao,
            emergencia_detectada,
            status_emergencia,
            data_hora
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (
        dados["cruzamento"],
        dados["veiculos"],
        dados["tempo_padrao"],
        dados["tempo_ia"],
        dados["tempo_sem_ia"],
        dados["tempo_com_ia"],
        dados["melhora"],
        dados["decisao"],
        1 if dados["emergencia"] else 0,
        dados["status_emergencia"],
        dados["data_hora"]
    ))

    conexao.commit()
    conexao.close()


def prever_tempo_com_ia(qtd_veiculos, emergencia, hora_pico):
    """
    Usa o modelo treinado de IA para prever o tempo ideal do semáforo.
    """

    if modelo_ia is None:
        # Regra de segurança caso o modelo não esteja carregado.
        if emergencia:
            return 45
        if qtd_veiculos <= 5:
            return 10
        if qtd_veiculos <= 15:
            return 20
        if qtd_veiculos <= 25:
            return 34
        return 45

    entrada = pd.DataFrame([{
        "veiculos": qtd_veiculos,
        "emergencia": 1 if emergencia else 0,
        "hora_pico": 1 if hora_pico else 0
    }])

    tempo_previsto = modelo_ia.predict(entrada)[0]
    tempo_previsto = round(float(tempo_previsto))

    # Limites usados na maquete.
    # Evita tempo muito baixo ou muito alto.
    tempo_previsto = max(10, min(45, tempo_previsto))

    return tempo_previsto


def gerar_mensagem_decisao(qtd_veiculos, emergencia, hora_pico):
    """
    Gera a explicação textual da decisão tomada pela IA.
    """

    if emergencia:
        return "Veículo de emergência detectado. Liberando corredor prioritário."

    if qtd_veiculos <= 5:
        return "Fluxo baixo. A IA reduziu o tempo verde."
    elif qtd_veiculos <= 15:
        if hora_pico:
            return "Fluxo normal em horário de pico. A IA ajustou o tempo para evitar acúmulo."
        return "Fluxo normal. A IA manteve um tempo intermediário."
    elif qtd_veiculos <= 25:
        return "Fluxo alto. A IA aumentou o tempo verde para melhorar a passagem."
    else:
        return "Fluxo intenso. A IA aplicou tempo maior para reduzir a fila."


def calcular_comparacao(qtd_veiculos, emergencia=False):
    """
    Compara o modelo convencional com o sistema inteligente.
    """

    if emergencia:
        tempo_sem_ia = 45
        tempo_com_ia = 10
    elif qtd_veiculos <= 5:
        tempo_sem_ia = 20
        tempo_com_ia = 18
    elif qtd_veiculos <= 15:
        tempo_sem_ia = 40
        tempo_com_ia = 32
    elif qtd_veiculos <= 25:
        tempo_sem_ia = 60
        tempo_com_ia = 42
    else:
        tempo_sem_ia = 85
        tempo_com_ia = 60

    melhora = ((tempo_sem_ia - tempo_com_ia) / tempo_sem_ia) * 100

    return tempo_sem_ia, tempo_com_ia, round(melhora, 1)


def gerar_dados_sistema():
    """
    Gera os dados exibidos no dashboard.

    A quantidade de veículos ainda é simulada.
    Depois será substituída pela contagem real com OpenCV.
    """

    global ciclos_emergencia

    cruzamento = 1
    veiculos_detectados = random.randint(3, 32)
    tempo_padrao = 20

    # Simulação simples de horário de pico.
    # Depois pode ser substituída pelo horário real do sistema.
    hora_pico = random.choice([False, True])

    emergencia = ciclos_emergencia > 0

    if emergencia:
        ciclos_emergencia -= 1

    tempo_ia = prever_tempo_com_ia(
        qtd_veiculos=veiculos_detectados,
        emergencia=emergencia,
        hora_pico=hora_pico
    )

    decisao = gerar_mensagem_decisao(
        qtd_veiculos=veiculos_detectados,
        emergencia=emergencia,
        hora_pico=hora_pico
    )

    tempo_sem_ia, tempo_com_ia, melhora = calcular_comparacao(
        qtd_veiculos=veiculos_detectados,
        emergencia=emergencia
    )

    if emergencia:
        status_emergencia = "Veículo de emergência detectado"
    else:
        status_emergencia = "Nenhuma emergência detectada"

    return {
        "cruzamento": cruzamento,
        "veiculos": veiculos_detectados,
        "tempo_padrao": tempo_padrao,
        "tempo_ia": tempo_ia,
        "tempo_sem_ia": tempo_sem_ia,
        "tempo_com_ia": tempo_com_ia,
        "melhora": melhora,
        "decisao": decisao,
        "emergencia": emergencia,
        "status_emergencia": status_emergencia,
        "hora_pico": hora_pico,
        "modelo_ia": "Decision Tree - Scikit-learn",
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status")
def status():
    dados = gerar_dados_sistema()
    salvar_registro(dados)
    return jsonify(dados)


@app.route("/api/historico")
def historico():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id_registro,
            cruzamento,
            veiculos_detectados,
            tempo_padrao,
            tempo_ia,
            tempo_sem_ia,
            tempo_com_ia,
            melhora_percentual,
            decisao,
            status_emergencia,
            data_hora
        FROM registros_dashboard
        ORDER BY id_registro DESC
        LIMIT 10;
    """)

    linhas = cursor.fetchall()
    conexao.close()

    registros = []

    for linha in linhas:
        registros.append({
            "id_registro": linha[0],
            "cruzamento": linha[1],
            "veiculos_detectados": linha[2],
            "tempo_padrao": linha[3],
            "tempo_ia": linha[4],
            "tempo_sem_ia": linha[5],
            "tempo_com_ia": linha[6],
            "melhora_percentual": linha[7],
            "decisao": linha[8],
            "status_emergencia": linha[9],
            "data_hora": linha[10]
        })

    return jsonify(registros)


@app.route("/api/simular_emergencia", methods=["POST"])
def simular_emergencia():
    """
    Ativa a emergência por algumas atualizações do dashboard.
    Futuramente será substituído pela leitura RFID.
    """

    global ciclos_emergencia
    ciclos_emergencia = 3

    return jsonify({
        "mensagem": "Emergência simulada ativada com sucesso."
    })


if __name__ == "__main__":
    criar_tabela_se_nao_existir()
    app.run(debug=True)