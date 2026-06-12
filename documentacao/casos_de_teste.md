# Casos de Teste do Sistema

| ID | Requisito | Cenário de Teste | Entrada | Resultado Esperado | Evidência | Status |
|---|---|---|---|---|---|---|
| CT01 | RF01 | Acessar dashboard web | Abrir `http://127.0.0.1:5000` | Dashboard carregado corretamente | Print do dashboard | Concluído |
| CT02 | RF02 | Consultar API de status | Acessar `/api/status` | Retorno JSON com dados do cruzamento | Print da API | Concluído |
| CT03 | RF03 | Registrar histórico | Atualização automática do dashboard | Dados salvos no banco SQLite | Print do histórico | Concluído |
| CT04 | RF04 | Executar modelo de IA | Rodar `testar_modelo.py` | Modelo retorna tempo previsto | Print do terminal | Concluído |
| CT05 | RF05 | Integrar IA ao dashboard | Carregar dashboard após integração | Exibição do modelo Decision Tree | Print do dashboard com IA | Concluído |
| CT06 | RF06 | Simular horário de pico | API retorna `hora_pico=true` | Dashboard exibe “Sim” em horário de pico | Print do dashboard/API | Concluído |
| CT07 | RF07 | Simular veículo de emergência | Clicar no botão de emergência | Sistema ativa prioridade de passagem | Print do dashboard emergência | Parcial |
| CT08 | RF08 | Consultar histórico dos registros | Acessar `/api/historico` | Lista de registros recentes retornada | Print do histórico/API | Concluído |