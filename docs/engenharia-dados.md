# 🛠️ Engenharia de Dados com Python

Nesta fase do projeto, implementamos um pipeline de processamento de dados utilizando **Python** e **Pandas** para substituir o tratamento pesado que anteriormente era realizado no Power Query.

## 🚀 Por que usar Python aqui?
- **Performance:** O Pandas processa milhares de linhas de forma muito mais eficiente que o Power BI Desktop.
- **Reprodutibilidade:** O script de limpeza pode ser versionado no Git e auditado.
- **Automação:** Facilidade para integrar novas rodadas de dados sem intervenção manual no Power BI.

## 📋 O que o script de Limpeza realiza:
O arquivo [`data_cleaning.py`](https://github.com/NandesLima/analise-campeonato-brasileiro/blob/main/data_cleaning.py) automatiza as seguintes etapas:

1.  **Tratamento de Nulos:** Preenche formações e técnicos ausentes com "Não Informado".
2.  **Cálculo de Pontuação:** Gera as colunas de pontos (3, 1 ou 0) com base no vencedor da partida.
3.  **Tipagem de Dados:** Garante que datas e placares estejam no formato correto para análise.
4.  **Feature Engineering:** Cria métricas de soma de gols e indicadores de mando de campo.

---
*Este processo garante que o Power BI receba dados "prontos para consumo", focando exclusivamente na visualização e storytelling.*
