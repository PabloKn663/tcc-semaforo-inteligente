# Dashboard do Sistema

Este arquivo documenta o funcionamento do dashboard do projeto de Semáforo Inteligente com Inteligência Artificial.

O dashboard é a interface principal do sistema nesta fase do desenvolvimento. Ele foi criado para facilitar a visualização dos dados gerados pela simulação, permitindo acompanhar o comportamento do semáforo inteligente em tempo real.

---

## Objetivo do Dashboard

O objetivo do dashboard é mostrar, de forma simples e visual, como o sistema está tomando decisões durante a simulação do trânsito.

Por meio dele, é possível acompanhar:

- quantidade de veículos detectados;
- tempo padrão do semáforo convencional;
- tempo calculado pelo sistema inteligente;
- comparação entre o sistema convencional e o sistema com IA;
- percentual de melhora estimada;
- decisão tomada pelo sistema;
- status de emergência;
- histórico dos registros salvos no banco de dados.

---

## Tecnologias Utilizadas

O dashboard utiliza as seguintes tecnologias:

- Python;
- Flask;
- HTML;
- CSS;
- JavaScript;
- SQLite.

O Flask é responsável por criar o servidor local e fornecer os dados para a página.

O HTML e o CSS são usados para estruturar e estilizar a interface.

O JavaScript atualiza os dados automaticamente na tela.

O SQLite armazena os registros gerados durante a simulação.

---

## Funcionamento Atual

Nesta versão, o dashboard utiliza dados simulados para representar a quantidade de veículos no cruzamento.

Essa escolha foi feita porque o projeto ainda está em fase inicial. Antes de integrar câmera, RFID e ESP32, foi necessário validar primeiro a estrutura principal do sistema:

1. geração dos dados;
2. cálculo dos tempos;
3. comparação entre semáforo comum e inteligente;
4. exibição das informações no dashboard;
5. salvamento dos registros no banco de dados.

Posteriormente, a quantidade de veículos simulada será substituída pela contagem real feita por câmera utilizando OpenCV.

---

## Informações Exibidas na Tela

Atualmente o dashboard exibe:

### Cruzamento

Mostra qual cruzamento está sendo monitorado na simulação.

### Veículos Detectados

Mostra a quantidade de veículos considerada pelo sistema naquele momento.

Nesta etapa, esse valor ainda é gerado de forma simulada pelo Python.

### Tempo Padrão

Representa o tempo fixo utilizado como base para comparação com o sistema inteligente.

### Tempo Calculado pelo Sistema Inteligente

Mostra o tempo definido pelo sistema com base na quantidade de veículos detectados.

### Tempo Estimado sem IA

Representa o tempo aproximado que o trânsito levaria em um modelo convencional de semáforo com tempo fixo.

### Tempo Estimado com IA

Representa o tempo aproximado com o sistema inteligente ajustando os tempos conforme o fluxo.

### Melhora Estimada

Mostra a porcentagem de melhora estimada entre o sistema convencional e o sistema inteligente.

### Decisão do Sistema

Exibe uma mensagem explicando a decisão tomada pelo sistema.

Exemplo:

- fluxo baixo: reduz o tempo verde;
- fluxo normal: mantém o tempo padrão;
- fluxo alto: aumenta o tempo verde;
- fluxo intenso: aplica tempo máximo configurado.

### Histórico

Mostra os últimos registros salvos no banco de dados SQLite.

---

## Rotas Disponíveis

### Dashboard principal

```text
/