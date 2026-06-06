CREATE TABLE cruzamento (
    id_cruzamento INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    localizacao TEXT
);

CREATE TABLE fluxo_trafego (
    id_fluxo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cruzamento INTEGER NOT NULL,
    quantidade_veiculos INTEGER NOT NULL,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cruzamento) REFERENCES cruzamento(id_cruzamento)
);

CREATE TABLE semaforo (
    id_semaforo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cruzamento INTEGER NOT NULL,
    status_atual TEXT NOT NULL,
    tempo_verde INTEGER NOT NULL,
    tempo_amarelo INTEGER NOT NULL,
    tempo_vermelho INTEGER NOT NULL,
    FOREIGN KEY (id_cruzamento) REFERENCES cruzamento(id_cruzamento)
);

CREATE TABLE veiculo_emergencia (
    id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_rfid TEXT NOT NULL UNIQUE,
    tipo_veiculo TEXT NOT NULL
);

CREATE TABLE decisao_ia (
    id_decisao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cruzamento INTEGER NOT NULL,
    quantidade_veiculos INTEGER NOT NULL,
    tempo_padrao INTEGER NOT NULL,
    tempo_calculado INTEGER NOT NULL,
    emergencia_detectada INTEGER NOT NULL,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cruzamento) REFERENCES cruzamento(id_cruzamento)
);