from flask import Flask, render_template, jsonify
from datetime import datetime
from pathlib import Path
import random
import sqlite3

app = Flask(__name__)


# ==========================================================
# CONFIGURAÇÃO DO BANCO DE DADOS
# ==========================================================

# Caminho da pasta principal do projeto
# Este arquivo está em: codigo/dashboard/app.py
# Então usamos parents[2] para voltar até a pasta principal.
PASTA_PROJETO = Path(__file__).resolve().parents[2]

# Caminho da pasta banco_de_dados
PASTA_BANCO = PASTA_PROJETO / "banco_de_dados"

# Caminho final do arquivo do banco
CAMINHO_BANCO = PASTA_BANCO / "semaforo_inteligente.db"


def conectar_banco():
    """
    Cria uma conexão com o banco SQLite.
    """
    return sqlite3.connect(CAMINHO_BANCO)


def criar_tabela_se_nao_existir():
    """
    Cria a tabela de registros do dashboard caso ela ainda não exista.
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
    Salva no banco os dados gerados pelo sistema.
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


# ==========================================================
# LÓGICA DA IA / SIMULAÇÃO
# ==========================================================

def calcular_tempo_ia(qtd_veiculos, emergencia=False):
    """
    Simula a decisão da Inteligência Artificial.

    Entrada:
    - quantidade de veículos detectados;
    - informação de emergência.

    Saída:
    - tempo ideal do semáforo;
    - mensagem explicando a decisão.
    """

    if emergencia:
        return 45, "Veículo de emergência detectado. Liberando corredor prioritário."

    if qtd_veiculos <= 5:
        return 10, "Fluxo baixo. A IA reduziu o tempo verde."
    elif qtd_veiculos <= 15:
        return 20, "Fluxo normal. A IA manteve o tempo padrão."
    elif qtd_veiculos <= 25:
        return 34, "A IA aumentou o tempo verde para melhorar o fluxo."
    else:
        return 45, "Fluxo intenso. A IA aplicou tempo máximo para reduzir a fila."


def calcular_comparacao(qtd_veiculos):
    """
    Simula a comparação entre semáforo convencional e semáforo inteligente.

    O sistema convencional trabalha com lógica fixa.
    O sistema inteligente ajusta o funcionamento conforme o fluxo.
    """

    if qtd_veiculos <= 5:
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
    melhora = round(melhora, 1)

    return tempo_sem_ia, tempo_com_ia, melhora


def gerar_dados_sistema():
    """
    Gera os dados simulados do sistema.

    Depois, a quantidade de veículos será substituída pela contagem real da câmera.
    """

    cruzamento = 1
    veiculos_detectados = random.randint(3, 32)
    tempo_padrao = 20
    emergencia = False

    tempo_ia, decisao = calcular_tempo_ia(veiculos_detectados, emergencia)
    tempo_sem_ia, tempo_com_ia, melhora = calcular_comparacao(veiculos_detectados)

    dados = {
        "cruzamento": cruzamento,
        "veiculos": veiculos_detectados,
        "tempo_padrao": tempo_padrao,
        "tempo_ia": tempo_ia,
        "tempo_sem_ia": tempo_sem_ia,
        "tempo_com_ia": tempo_com_ia,
        "melhora": melhora,
        "decisao": decisao,
        "emergencia": emergencia,
        "status_emergencia": "Nenhuma emergência detectada",
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return dados


# ==========================================================
# ROTAS DO FLASK
# ==========================================================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status")
def status():
    """
    Rota usada pelo dashboard.

    Toda vez que o dashboard atualiza, esta rota:
    1. gera os dados;
    2. salva no banco;
    3. envia os dados para a tela.
    """

    dados = gerar_dados_sistema()
    salvar_registro(dados)

    return jsonify(dados)


@app.route("/api/historico")
def historico():
    """
    Mostra os últimos registros salvos no banco.
    Esta rota serve para testar se o banco está funcionando.
    """

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


# ==========================================================
# INICIALIZAÇÃO DO SISTEMA
# ==========================================================

if __name__ == "__main__":
    criar_tabela_se_nao_existir()
    app.run(debug=True)