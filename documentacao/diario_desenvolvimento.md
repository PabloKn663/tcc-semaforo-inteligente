# Diário de Desenvolvimento

Este arquivo registra a evolução técnica do projeto ao longo do desenvolvimento.

---

## Etapa 1 - Organização inicial do projeto

Foi criada a estrutura inicial de pastas do projeto, separando código, banco de dados, documentação, imagens, referências e testes.

Essa organização foi adotada para facilitar o desenvolvimento em grupo e manter o projeto mais fácil de consultar.

---

## Etapa 2 - Criação do dashboard inicial

Foi desenvolvido um dashboard local utilizando Flask, HTML, CSS e JavaScript.

A primeira versão do dashboard apresenta:

- quantidade de veículos detectados;
- tempo padrão do semáforo;
- tempo calculado pelo sistema inteligente;
- decisão tomada pelo sistema;
- status de emergência;
- data e hora do registro.

---

## Etapa 3 - Comparação entre sistema convencional e inteligente

Foi adicionada uma comparação entre o funcionamento de um semáforo convencional e o funcionamento do sistema inteligente.

Essa comparação permite visualizar:

- tempo estimado sem IA;
- tempo estimado com IA;
- percentual de melhora;
- barras comparativas no dashboard.

Nesta fase, os valores ainda são simulados para permitir a validação da lógica antes da integração com câmera e sensores.

---

## Etapa 4 - Integração com banco de dados

Foi integrado um banco SQLite para armazenar os registros gerados durante a simulação.

Cada registro salva informações como:

- quantidade de veículos;
- tempo padrão;
- tempo calculado pelo sistema;
- tempo estimado sem IA;
- tempo estimado com IA;
- percentual de melhora;
- decisão tomada;
- data e hora.

---

## Etapa 5 - Histórico no dashboard

Foi adicionada uma tabela no dashboard para exibir os últimos registros salvos no banco.

Essa funcionalidade ajuda na análise dos testes e permite acompanhar a evolução das simulações durante a execução do sistema.

---

## Próximas etapas

As próximas etapas previstas são:

- criar o modo de emergência simulado;
- integrar o RFID RC522;
- integrar o ESP32 com LEDs físicos;
- iniciar testes com OpenCV;
- substituir os dados simulados por contagem real de veículos.

---

## Etapa 6 - Modo emergência simulado

Foi adicionado um modo de emergência simulado no dashboard.

Essa função permite testar o comportamento do sistema antes da integração física com o RFID RC522.

Ao clicar no botão de emergência, o sistema altera temporariamente o status do cruzamento para emergência, calcula prioridade de passagem e registra o evento no banco de dados.

Mais adiante, esse botão será substituído pela leitura real da tag RFID instalada no veículo prioritário da maquete.