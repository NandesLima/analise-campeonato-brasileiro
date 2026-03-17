# ⚽ Dashboard Esportivo: Campeonato Brasileiro (Série A)

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" />
</div>

<br>

> ⚠️ **UPGRADE DE STACK (Refatoração):** Este projeto original em Power BI foi refatorado para demonstrar a transição de um workflow manual para um **Pipeline Híbrido de Dados**. O Power BI agora serve como camada de visualização histórica, enquanto toda a inteligência de tratamento e análise estatística foi migrada para **Python & Pandas**.

---

## 🚀 Por que Refatorar?
A decisão de refatorar este projeto legado visou:
1.  **Versionamento de Código:** Migrar o ETL do Power Query para Python permite o controle de versão real via Git.
2.  **Performance:** Processamento de dados programático é mais veloz e escalável.
3.  **Profundidade Analítica:** Adição de EDA (Análise Exploratória de Dados) com visualizações estatísticas (Seaborn/Matplotlib) que superam as limitações de dashboards executivos.

---

## 📋 Arquitetura do Projeto
- **Visualização Legada:** Dashboards interativos no Power BI (ver `docs/assets`).
- **Engenharia de Dados:** Script [`data_cleaning.py`](data_cleaning.py) para limpeza e Feature Engineering.
- **Ciência de Dados:** Script [`data_viz.py`](data_viz.py) para análises estatísticas e geração de gráficos de tendência.
- **Documentação:** Site interativo gerado via **MkDocs**.

👉 **[Acesse o Site Completo do Projeto](https://nandeslima.github.io/analise-campeonato-brasileiro/)**
