# Modelo Lógico do Banco de Dados

O modelo lógico apresenta as tabelas principais do sistema e seus relacionamentos, sem depender diretamente de um banco específico.

Nesta etapa, o protótipo utiliza SQLite por ser mais simples para testes locais. Porém, a modelagem foi pensada para permitir evolução futura para PostgreSQL, com tabelas separadas e relacionamentos normalizados.

## CRUZAMENTO

CRUZAMENTO(
id_cruzamento PK,
nome,
localizacao,
descricao
)

A tabela CRUZAMENTO representa o local monitorado pelo sistema. Cada cruzamento pode possuir semáforos, registros de tráfego e alertas associados.

## SEMAFORO

SEMAFORO(
id_semaforo PK,
id_cruzamento FK,
identificacao,
tempo_padrao,
status_atual
)

A tabela SEMAFORO armazena os semáforos vinculados a cada cruzamento. O campo tempo_padrao representa o tempo fixo usado como base para comparação com o sistema inteligente.

## LOG_TRAFEGO

LOG_TRAFEGO(
id_log PK,
id_cruzamento FK,
quantidade_veiculos,
intensidade_fluxo,
data_hora
)

A tabela LOG_TRAFEGO registra as informações de fluxo do cruzamento, como a quantidade de veículos detectados e a intensidade do trânsito.

## DECISAO_IA

DECISAO_IA(
id_decisao PK,
id_log FK,
tempo_calculado,
tempo_sem_ia,
tempo_com_ia,
melhora_percentual,
decisao,
data_hora
)

A tabela DECISAO_IA armazena a decisão calculada pelo modelo de Inteligência Artificial. Ela registra o tempo recomendado, a comparação com o modelo convencional e a justificativa da decisão tomada.

## VEICULOS_EMERGENCIA

VEICULOS_EMERGENCIA(
id_veiculo PK,
codigo_rfid,
tipo_veiculo,
descricao,
ativo
)

A tabela VEICULOS_EMERGENCIA armazena os veículos prioritários cadastrados no sistema, identificados por tag RFID.

## HISTORICO_ALERTAS

HISTORICO_ALERTAS(
id_alerta PK,
id_veiculo FK,
id_cruzamento FK,
tipo_alerta,
status_alerta,
data_hora
)

A tabela HISTORICO_ALERTAS registra eventos importantes, como detecção de emergência, fluxo intenso ou outras situações relevantes para auditoria do sistema.

## Relacionamentos

* Um cruzamento pode possuir vários semáforos.
* Um cruzamento pode possuir vários registros de tráfego.
* Um registro de tráfego pode gerar uma decisão da IA.
* Um veículo de emergência pode gerar vários alertas.
* Um cruzamento pode possuir vários alertas.
