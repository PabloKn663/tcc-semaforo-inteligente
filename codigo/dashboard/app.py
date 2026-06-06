from flask import Flask, render_template, jsonify
from datetime import datetime
from pathlib import Path
import random
import sqlite3

app = Flask(__name__)


# Caminho do banco de dados.
# Como o app.py está dentro de codigo/dashboard, voltamos duas pastas
# para chegar na raiz do projeto.
PASTA_PROJETO = Path(__file__).resolve().parents[2]
PASTA_BANCO = PASTA_PROJETO / "banco_de_dados"
CAMINHO_BANCO = PASTA_BANCO / "semaforo_inteligente.db"


def conectar_banco():
    return sqlite3.connect(CAMINHO_BANCO)


def criar_tabela_se_nao_existir():
    """
    Cria a tabela usada pelo dashboard.

    Por enquanto estamos usando uma tabela única para facilitar os testes.
    Na documentação do TCC, essa modelagem pode evoluir para tabelas separadas.
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
    Isso ajuda a criar um histórico para os testes do projeto.
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


def calcular_tempo_semaforo(qtd_veiculos, emergencia=False):
    """
    Define o tempo do semáforo com base na quantidade de veículos.

    Nesta fase, essa regra representa a lógica inicial do sistema.
    Depois ela poderá ser substituída ou ajustada com um modelo de IA treinado.
    """

    if emergencia:
        return 45, "Veículo de emergência detectado. Liberando corredor prioritário."

    if qtd_veiculos <= 5:
        return 10, "Fluxo baixo. O sistema reduziu o tempo verde."
    elif qtd_veiculos <= 15:
        return 20, "Fluxo normal. O sistema manteve o tempo padrão."
    elif qtd_veiculos <= 25:
        return 34, "Fluxo alto. O sistema aumentou o tempo verde para melhorar a passagem."
    else:
        return 45, "Fluxo intenso. O sistema aplicou o tempo máximo configurado."


def calcular_comparacao(qtd_veiculos):
    """
    Compara uma situação de semáforo comum com o sistema inteligente.

    Os valores são simulados para esta etapa do protótipo.
    A ideia é mostrar no dashboard o ganho esperado com a adaptação dos tempos.
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
    return tempo_sem_ia, tempo_com_ia, round(melhora, 1)


def gerar_dados_sistema():
    """
    Gera os dados usados pelo dashboard.

    Por enquanto, a quantidade de veículos é simulada.
    Quando a câmera for integrada, esse número virá da contagem feita com OpenCV.
    """

    cruzamento = 1
    veiculos_detectados = random.randint(3, 32)
    tempo_padrao = 20
    emergencia = False

    tempo_ia, decisao = calcular_tempo_semaforo(veiculos_detectados, emergencia)
    tempo_sem_ia, tempo_com_ia, melhora = calcular_comparacao(veiculos_detectados)

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
        "status_emergencia": "Nenhuma emergência detectada",
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


if __name__ == "__main__":
    criar_tabela_se_nao_existir()
    app.run(debug=True)