# Decisões Técnicas do Projeto

Este documento registra as principais decisões técnicas adotadas no projeto até o momento.

---

## Uso do Flask

O Flask foi escolhido por ser uma ferramenta simples para criar aplicações web em Python.

Como o projeto ainda está em fase de protótipo, o Flask atende bem à necessidade de criar um dashboard local para visualização dos dados do sistema.

---

## Uso do SQLite

O SQLite foi escolhido nesta fase porque não exige instalação de servidor de banco de dados.

Isso facilita os testes iniciais e permite salvar os registros do sistema diretamente em um arquivo local.

Em uma versão futura, o banco poderá ser migrado para PostgreSQL caso o projeto precise de uma estrutura mais robusta.

---

## Uso de dados simulados

Nesta etapa inicial, a quantidade de veículos ainda é simulada pelo sistema.

Essa escolha foi feita para permitir o desenvolvimento do dashboard, do banco de dados e da lógica de decisão antes da integração com a câmera.

Mais adiante, esses valores serão substituídos pela contagem real de veículos utilizando OpenCV.

---

## Uso de comparação com e sem IA

A comparação entre o sistema convencional e o sistema inteligente foi adicionada para facilitar a visualização dos ganhos esperados.

Com isso, o dashboard mostra de forma mais clara a diferença entre um semáforo de tempo fixo e um sistema adaptativo.

---

## Uso futuro do OpenCV

O OpenCV será utilizado para capturar imagens da maquete e contar os veículos presentes em cada cruzamento.

A câmera será posicionada acima da via, permitindo uma visão melhor do fluxo de trânsito.

---

## Uso futuro do RFID

O RFID será utilizado para simular a identificação de veículos de emergência.

Na maquete, uma tag RFID será colocada no veículo prioritário, e o leitor RC522 será posicionado próximo ao cruzamento.

Quando o sistema detectar a tag, o semáforo deverá liberar a passagem do veículo.

---

## Uso futuro do ESP32

O ESP32 será utilizado para controlar os LEDs dos semáforos físicos da maquete.

Ele foi escolhido por ter baixo custo, boa disponibilidade e facilidade de integração com projetos acadêmicos.