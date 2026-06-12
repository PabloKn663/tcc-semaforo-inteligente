# Dicionário de Dados

Este dicionário apresenta os principais dados utilizados na modelagem proposta para o sistema de semáforo inteligente.

Embora o protótipo atual utilize SQLite para facilitar os testes locais, a modelagem apresentada considera uma estrutura normalizada, podendo ser evoluída para PostgreSQL em uma versão futura.

## Tabela: CRUZAMENTO

| Campo         | Tipo         | Restrição    | Descrição                                     |
| ------------- | ------------ | ------------ | --------------------------------------------- |
| id_cruzamento | INTEGER      | PK, NOT NULL | Identificador único do cruzamento.            |
| nome          | VARCHAR(100) | NOT NULL     | Nome ou identificação do cruzamento.          |
| localizacao   | VARCHAR(150) | NULL         | Localização ou descrição do ponto monitorado. |
| descricao     | TEXT         | NULL         | Observações gerais sobre o cruzamento.        |

## Tabela: SEMAFORO

| Campo         | Tipo        | Restrição           | Descrição                                                  |
| ------------- | ----------- | ------------------- | ---------------------------------------------------------- |
| id_semaforo   | INTEGER     | PK, NOT NULL        | Identificador único do semáforo.                           |
| id_cruzamento | INTEGER     | FK, NOT NULL        | Cruzamento ao qual o semáforo pertence.                    |
| identificacao | VARCHAR(50) | NOT NULL            | Nome ou código do semáforo.                                |
| tempo_padrao  | INTEGER     | NOT NULL, CHECK > 0 | Tempo fixo usado como referência convencional.             |
| status_atual  | VARCHAR(20) | NOT NULL            | Estado atual do semáforo, como verde, amarelo ou vermelho. |

## Tabela: LOG_TRAFEGO

| Campo               | Tipo        | Restrição            | Descrição                                               |
| ------------------- | ----------- | -------------------- | ------------------------------------------------------- |
| id_log              | INTEGER     | PK, NOT NULL         | Identificador do registro de tráfego.                   |
| id_cruzamento       | INTEGER     | FK, NOT NULL         | Cruzamento relacionado ao registro.                     |
| quantidade_veiculos | INTEGER     | NOT NULL, CHECK >= 0 | Quantidade de veículos detectados.                      |
| intensidade_fluxo   | VARCHAR(20) | NOT NULL             | Classificação do fluxo: baixo, normal, alto ou intenso. |
| data_hora           | TIMESTAMP   | NOT NULL             | Data e hora do registro.                                |

## Tabela: DECISAO_IA

| Campo              | Tipo         | Restrição           | Descrição                                         |
| ------------------ | ------------ | ------------------- | ------------------------------------------------- |
| id_decisao         | INTEGER      | PK, NOT NULL        | Identificador da decisão tomada pelo sistema.     |
| id_log             | INTEGER      | FK, NOT NULL        | Registro de tráfego usado como entrada para a IA. |
| tempo_calculado    | INTEGER      | NOT NULL, CHECK > 0 | Tempo recomendado pela IA para o semáforo.        |
| tempo_sem_ia       | INTEGER      | NOT NULL, CHECK > 0 | Tempo estimado no modelo convencional.            |
| tempo_com_ia       | INTEGER      | NOT NULL, CHECK > 0 | Tempo estimado no modelo inteligente.             |
| melhora_percentual | NUMERIC(5,2) | CHECK >= 0          | Percentual estimado de melhoria no fluxo.         |
| decisao            | TEXT         | NOT NULL            | Texto explicando a decisão do sistema.            |
| data_hora          | TIMESTAMP    | NOT NULL            | Data e hora da decisão.                           |

## Tabela: VEICULOS_EMERGENCIA

| Campo        | Tipo         | Restrição        | Descrição                                              |
| ------------ | ------------ | ---------------- | ------------------------------------------------------ |
| id_veiculo   | INTEGER      | PK, NOT NULL     | Identificador do veículo de emergência.                |
| codigo_rfid  | VARCHAR(100) | UNIQUE, NOT NULL | Código da tag RFID associada ao veículo.               |
| tipo_veiculo | VARCHAR(50)  | NOT NULL         | Tipo do veículo, como ambulância, polícia ou bombeiro. |
| descricao    | TEXT         | NULL             | Observações sobre o veículo.                           |
| ativo        | BOOLEAN      | NOT NULL         | Indica se a tag RFID está ativa no sistema.            |

## Tabela: HISTORICO_ALERTAS

| Campo         | Tipo        | Restrição    | Descrição                                              |
| ------------- | ----------- | ------------ | ------------------------------------------------------ |
| id_alerta     | INTEGER     | PK, NOT NULL | Identificador do alerta registrado.                    |
| id_veiculo    | INTEGER     | FK, NULL     | Veículo de emergência relacionado ao alerta.           |
| id_cruzamento | INTEGER     | FK, NOT NULL | Cruzamento onde o alerta ocorreu.                      |
| tipo_alerta   | VARCHAR(50) | NOT NULL     | Tipo do alerta, como emergência ou fluxo intenso.      |
| status_alerta | VARCHAR(30) | NOT NULL     | Situação do alerta, como ativo, tratado ou finalizado. |
| data_hora     | TIMESTAMP   | NOT NULL     | Data e hora em que o alerta foi registrado.            |
