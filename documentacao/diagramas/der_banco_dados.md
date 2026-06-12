# DER - Diagrama de Entidades e Relacionamentos

```mermaid
erDiagram

    CRUZAMENTO ||--o{ SEMAFORO : possui
    CRUZAMENTO ||--o{ LOG_TRAFEGO : registra
    LOG_TRAFEGO ||--|| DECISAO_IA : gera
    CRUZAMENTO ||--o{ HISTORICO_ALERTAS : possui
    VEICULOS_EMERGENCIA ||--o{ HISTORICO_ALERTAS : gera

    CRUZAMENTO {
        int id_cruzamento PK
        string nome
        string localizacao
        string descricao
    }

    SEMAFORO {
        int id_semaforo PK
        int id_cruzamento FK
        string identificacao
        int tempo_padrao
        string status_atual
    }

    LOG_TRAFEGO {
        int id_log PK
        int id_cruzamento FK
        int quantidade_veiculos
        string intensidade_fluxo
        datetime data_hora
    }

    DECISAO_IA {
        int id_decisao PK
        int id_log FK
        int tempo_calculado
        int tempo_sem_ia
        int tempo_com_ia
        decimal melhora_percentual
        string decisao
        datetime data_hora
    }

    VEICULOS_EMERGENCIA {
        int id_veiculo PK
        string codigo_rfid
        string tipo_veiculo
        string descricao
        boolean ativo
    }

    HISTORICO_ALERTAS {
        int id_alerta PK
        int id_veiculo FK
        int id_cruzamento FK
        string tipo_alerta
        string status_alerta
        datetime data_hora
    }