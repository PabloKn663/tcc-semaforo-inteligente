-- Modelo físico proposto para o sistema de semáforo inteligente.
-- Nesta fase o protótipo usa SQLite, mas esta estrutura foi criada
-- pensando em uma evolução futura para PostgreSQL.

CREATE TABLE cruzamento (
    id_cruzamento SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    localizacao VARCHAR(150),
    descricao TEXT
);

CREATE TABLE semaforo (
    id_semaforo SERIAL PRIMARY KEY,
    id_cruzamento INTEGER NOT NULL,
    identificacao VARCHAR(50) NOT NULL,
    tempo_padrao INTEGER NOT NULL CHECK (tempo_padrao > 0),
    status_atual VARCHAR(20) NOT NULL CHECK (
        status_atual IN ('verde', 'amarelo', 'vermelho', 'desligado')
    ),

    CONSTRAINT fk_semaforo_cruzamento
        FOREIGN KEY (id_cruzamento)
        REFERENCES cruzamento(id_cruzamento)
);

CREATE TABLE log_trafego (
    id_log SERIAL PRIMARY KEY,
    id_cruzamento INTEGER NOT NULL,
    quantidade_veiculos INTEGER NOT NULL CHECK (quantidade_veiculos >= 0),
    intensidade_fluxo VARCHAR(20) NOT NULL CHECK (
        intensidade_fluxo IN ('baixo', 'normal', 'alto', 'intenso')
    ),
    data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_log_cruzamento
        FOREIGN KEY (id_cruzamento)
        REFERENCES cruzamento(id_cruzamento)
);

CREATE TABLE decisao_ia (
    id_decisao SERIAL PRIMARY KEY,
    id_log INTEGER NOT NULL,
    tempo_calculado INTEGER NOT NULL CHECK (tempo_calculado > 0),
    tempo_sem_ia INTEGER NOT NULL CHECK (tempo_sem_ia > 0),
    tempo_com_ia INTEGER NOT NULL CHECK (tempo_com_ia > 0),
    melhora_percentual NUMERIC(5,2) CHECK (melhora_percentual >= 0),
    decisao TEXT NOT NULL,
    data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_decisao_log
        FOREIGN KEY (id_log)
        REFERENCES log_trafego(id_log)
);

CREATE TABLE veiculos_emergencia (
    id_veiculo SERIAL PRIMARY KEY,
    codigo_rfid VARCHAR(100) NOT NULL UNIQUE,
    tipo_veiculo VARCHAR(50) NOT NULL CHECK (
        tipo_veiculo IN ('ambulancia', 'policia', 'bombeiro', 'outro')
    ),
    descricao TEXT,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE historico_alertas (
    id_alerta SERIAL PRIMARY KEY,
    id_veiculo INTEGER,
    id_cruzamento INTEGER NOT NULL,
    tipo_alerta VARCHAR(50) NOT NULL,
    status_alerta VARCHAR(30) NOT NULL CHECK (
        status_alerta IN ('ativo', 'tratado', 'finalizado')
    ),
    data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_alerta_veiculo
        FOREIGN KEY (id_veiculo)
        REFERENCES veiculos_emergencia(id_veiculo),

    CONSTRAINT fk_alerta_cruzamento
        FOREIGN KEY (id_cruzamento)
        REFERENCES cruzamento(id_cruzamento)
);