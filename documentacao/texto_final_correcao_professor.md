# Adequação dos Artefatos Técnicos do Projeto

Após a análise das observações realizadas pelo professor, o projeto foi revisado com foco na inclusão dos artefatos obrigatórios de Engenharia de Software, Modelagem UML, Arquitetura do Sistema, Banco de Dados, Casos de Teste e Cronograma.

A proposta do sistema foi mantida, porém a documentação técnica foi ampliada para demonstrar com mais clareza como o protótipo foi estruturado e como poderá evoluir nas próximas etapas.

## Engenharia de Software e UML

Foi criada a modelagem UML por meio do Diagrama de Casos de Uso, identificando os principais atores do sistema e suas interações.

Os atores definidos foram:

* Operador ou Administrador;
* Sistema de Visão Computacional com OpenCV;
* Veículo de Emergência identificado por RFID;
* Motor de Inteligência Artificial.

Os principais casos de uso definidos foram:

* monitorar dashboard;
* consultar status do cruzamento;
* contar veículos;
* classificar fluxo;
* calcular tempo do semáforo;
* registrar histórico;
* detectar veículo de emergência;
* liberar corredor prioritário;
* consultar histórico;
* executar teste da IA.

Essa modelagem foi adicionada para representar de forma visual as funcionalidades do sistema e facilitar o entendimento das responsabilidades de cada módulo.

## Arquitetura do Sistema

A arquitetura do sistema foi organizada em camadas, separando os módulos de captura, processamento, inteligência artificial, backend, banco de dados, dashboard e componentes físicos da maquete.

Na versão atual do protótipo, foram implementados:

* backend em Python com Flask;
* dashboard web com HTML, CSS e JavaScript;
* banco de dados local SQLite;
* modelo de IA com Decision Tree e Scikit-learn;
* simulação de fluxo de veículos;
* simulação de horário de pico;
* simulação de veículo de emergência;
* histórico de registros no banco de dados.

Para a evolução futura do projeto, foi proposta uma arquitetura mais robusta, com possibilidade de uso de PostgreSQL, MQTT, ESP32, RFID RC522, OpenCV e hospedagem em nuvem.

A aplicação mobile foi formalmente retirada do escopo desta etapa, pois o acompanhamento do sistema será realizado por meio do dashboard web.

## Banco de Dados

A modelagem do banco de dados foi reestruturada para evitar o uso de uma tabela única e genérica. Foi criado um modelo relacional normalizado, separando as principais entidades do sistema.

As tabelas propostas foram:

* CRUZAMENTO;
* SEMAFORO;
* LOG_TRAFEGO;
* DECISAO_IA;
* VEICULOS_EMERGENCIA;
* HISTORICO_ALERTAS.

Também foram criados o DER, o modelo lógico, o dicionário de dados e o modelo físico em PostgreSQL, contendo chaves primárias, chaves estrangeiras, restrições NOT NULL, UNIQUE e CHECK.

No protótipo atual, o SQLite continua sendo utilizado por ser mais simples para testes locais. Porém, a modelagem apresentada permite evolução futura para PostgreSQL.

## Inteligência Artificial

O projeto passou a contar com um modelo inicial de Inteligência Artificial treinado com a biblioteca Scikit-learn.

O algoritmo escolhido foi a Árvore de Decisão, por ser simples de interpretar e adequado para a fase inicial do protótipo.

O modelo foi treinado com dados simulados, utilizando como entradas:

* quantidade de veículos;
* presença de emergência;
* horário de pico.

A saída do modelo corresponde ao tempo recomendado para abertura do semáforo.

Após o treinamento, o modelo foi salvo no arquivo:

`codigo/ia/modelos/modelo_tempo_semaforo.pkl`

Em seguida, foi integrado ao backend Flask e passou a ser utilizado pelo dashboard para calcular o tempo inteligente do semáforo.

## Casos de Teste

Foi criada uma matriz de casos de teste para validar o funcionamento do protótipo.

Os testes contemplam:

* abertura do dashboard;
* consulta da API de status;
* consulta do histórico;
* execução do modelo de IA;
* integração da IA ao dashboard;
* exibição do horário de pico;
* simulação de emergência;
* registro de histórico no banco.

Cada caso de teste possui ID, requisito relacionado, cenário, entrada, resultado esperado, evidência e status.

## Cronograma

Foi criado um cronograma de evolução do TCC II, contemplando as etapas de documentação, requisitos, UML, banco de dados, dashboard, IA, OpenCV, ESP32, RFID, testes e apresentação final.

Esse cronograma permite visualizar o que já foi concluído, o que está em andamento e o que ainda será desenvolvido nas próximas fases do projeto.

## Evidências

Foram salvos prints do desenvolvimento e dos testes realizados, incluindo:

* treinamento da IA;
* teste do modelo Decision Tree;
* API retornando o modelo de IA;
* dashboard exibindo o modelo de IA;
* histórico de registros;
* comparação entre modelo convencional e modelo inteligente.

Essas evidências foram organizadas na pasta:

`documentacao/prints/`

Com isso, o projeto passa a apresentar os artefatos técnicos solicitados pelo professor, demonstrando de forma mais clara a estrutura, funcionamento, validação e evolução do sistema.
