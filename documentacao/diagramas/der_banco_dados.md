# Diagrama Entidade-Relacionamento do Banco de Dados

```mermaid
erDiagram

    VEICULOS_EMERGENCIA {
        int id PK
        string codigo_tag
        string tipo_veiculo
        string descricao
        string status
        datetime data_cadastro
    }

    LOG_TRAFEGO {
        int id PK
        int cruzamento
        int quantidade_veiculos
        string nivel_fluxo
        boolean horario_pico
        datetime data_hora
    }

    ESTADO_SEMAFORO {
        int id PK
        int log_trafego_id FK
        int tempo_padrao
        int tempo_calculado_ia
        int tempo_sem_ia
        int tempo_com_ia
        float melhoria_percentual
        string decisao_ia
        string modelo_ia
        datetime data_hora
    }

    HISTORICO_ALERTAS {
        int id PK
        int veiculo_emergencia_id FK
        int log_trafego_id FK
        string tipo_alerta
        string descricao
        string status
        datetime data_hora
    }

    LOG_TRAFEGO ||--o{ ESTADO_SEMAFORO : gera
    VEICULOS_EMERGENCIA ||--o{ HISTORICO_ALERTAS : aciona
    LOG_TRAFEGO ||--o{ HISTORICO_ALERTAS : registra