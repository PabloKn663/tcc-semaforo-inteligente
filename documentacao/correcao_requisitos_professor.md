# Correção dos Requisitos Técnicos Solicitados pelo Professor

## 1. Engenharia de Software e Modelagem UML

Esta seção apresenta os artefatos de Engenharia de Software adicionados ao projeto, com o objetivo de atender às exigências de modelagem, documentação técnica e validação do protótipo.

Foram incluídos os seguintes artefatos:

- Diagrama de Casos de Uso UML;
- Especificação dos atores do sistema;
- Detalhamento dos casos de uso;
- Tabela de requisitos funcionais e não funcionais;
- Plano de testes associado aos requisitos;
- Evidências de funcionamento do protótipo.

---

## 2. Arquitetura do Sistema

O sistema proposto é composto por módulos de visão computacional, inteligência artificial, backend, dashboard web, banco de dados e componentes físicos da maquete.

A arquitetura foi organizada em camadas para facilitar o entendimento do fluxo de dados, desde a captura das informações no ambiente físico até a exibição dos resultados no dashboard.

### 2.1 Arquitetura implementada no protótipo

Na versão atual do protótipo, foram implementados os seguintes componentes:

- Backend em Python com Flask;
- Dashboard web com HTML, CSS e JavaScript;
- Banco de dados local SQLite;
- Modelo de Inteligência Artificial com Decision Tree utilizando Scikit-learn;
- Simulação de quantidade de veículos;
- Simulação de horário de pico;
- Simulação de veículo de emergência;
- Registro de histórico no banco de dados;
- Exibição dos dados em dashboard web.

### 2.2 Arquitetura proposta para evolução final

Para uma versão mais robusta do sistema, a arquitetura poderá ser evoluída para:

- Backend em Python com FastAPI;
- Frontend em React.js;
- Banco de dados PostgreSQL;
- Comunicação MQTT com broker Mosquitto;
- ESP32 para controle dos LEDs do semáforo;
- RFID RC522 para identificação de veículos de emergência;
- OpenCV para contagem real de veículos por câmera;
- Hospedagem em nuvem para acesso remoto ao dashboard e às APIs.

### 2.3 Escopo mobile

Aplicação mobile não faz parte do escopo desta etapa do projeto. A visualização dos dados será realizada por meio de dashboard web acessado pelo navegador.

---

## 3. Banco de Dados e Modelagem Relacional

A modelagem de dados foi reorganizada para atender à exigência de separação das entidades principais do sistema.

Embora o protótipo atual utilize SQLite para facilitar os testes locais, a modelagem final será apresentada de forma normalizada, permitindo evolução futura para PostgreSQL.

As principais entidades do sistema são:

- CRUZAMENTO;
- SEMAFORO;
- LOG_TRAFEGO;
- DECISAO_IA;
- VEICULOS_EMERGENCIA;
- HISTORICO_ALERTAS.

---

## 4. Inteligência Artificial

O projeto passou a utilizar um modelo inicial de Inteligência Artificial baseado em Árvore de Decisão.

O modelo foi treinado com dados simulados, representando diferentes cenários de trânsito no cruzamento, considerando:

- quantidade de veículos;
- presença de veículo de emergência;
- horário de pico.

A saída do modelo corresponde ao tempo recomendado para abertura do semáforo.

O modelo foi treinado com a biblioteca Scikit-learn e salvo no arquivo:

`codigo/ia/modelos/modelo_tempo_semaforo.pkl`

Após o treinamento, o modelo foi integrado ao backend Flask e passou a ser utilizado pelo dashboard para calcular o tempo inteligente do semáforo.

---

## 5. Casos de Teste

Foram definidos casos de teste para validar o funcionamento do protótipo, incluindo dashboard, API, banco de dados, modelo de IA e simulação de emergência.

---

## 6. Cronograma

Foi definido um cronograma de evolução do projeto, contemplando documentação, desenvolvimento, integração com hardware, testes e apresentação final.

---

## 7. Evidências

As evidências do desenvolvimento foram salvas na pasta:

`documentacao/prints/`

Incluindo prints do treinamento da IA, teste do modelo, API, dashboard e integração da IA ao sistema.

---

## 8. Arquivos adicionados na correção

Foram adicionados os seguintes arquivos técnicos ao projeto:

- `documentacao/diagramas/arquitetura_sistema.md`
- `documentacao/diagramas/der_banco_dados.md`
- `documentacao/diagramas/casos_uso.md`
- `documentacao/dicionario_dados.md`
- `documentacao/modelo_logico_banco.md`
- `banco_de_dados/modelo_fisico_postgresql.sql`
- `documentacao/casos_de_teste.md`
- `documentacao/cronograma.md`
- `documentacao/texto_final_correcao_professor.md`

Esses arquivos atendem aos pontos solicitados pelo professor em relação à arquitetura, UML, banco de dados, testes, cronograma e evidências.