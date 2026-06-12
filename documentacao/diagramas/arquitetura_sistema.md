# Diagrama de Arquitetura do Sistema

```mermaid
flowchart TD

    A[Câmera / Webcam] --> B[OpenCV - Contagem de Veículos]
    B --> C[Motor de IA - Decision Tree]
    C --> D[Backend Python Flask]
    D --> E[Dashboard Web HTML CSS JavaScript]
    D --> F[Banco de Dados SQLite]

    G[Veículo de Emergência com Tag RFID] --> H[Leitor RFID RC522]
    H --> I[ESP32]
    I --> D

    D --> J[Controle dos LEDs do Semáforo]
    J --> K[Semáforo da Maquete]

    F --> L[Histórico de Registros]
    E --> L