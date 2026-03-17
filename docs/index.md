# ⚽ Brasileirão Analytics: Da Engenharia à Ciência de Dados

!!! quote "A Regra de Ouro"
    "Os dados não mentem, mas sozinhos eles não contam a história completa." — **Ariel Shlomoh**

Este projeto representa uma jornada completa de **Data Analytics**, saindo de um legado de planilhas para um pipeline moderno de engenharia de dados em Python, culminando em visualizações de alta performance e análises estatísticas avançadas.

---

## 🚀 O Diferencial deste Projeto

Diferente de dashboards convencionais, aqui tratamos o futebol como um ecossistema de dados complexos. Refatoramos toda a infraestrutura para garantir escalabilidade e precisão.

### 🛡️ Engenharia de Dados (Python)
Utilizamos Python e Pandas para criar um pipeline de limpeza robusto, processando mais de **7.600 partidas**. 
- **Normalização Automática:** Tratamento de nomes de clubes e técnicos.
- **Feature Engineering:** Cálculo dinâmico de pontos e fator de mando de campo direto no script.

### 📊 Dashboard Interativo (Power BI)
Uma experiência visual intuitiva para gestores esportivos e analistas de desempenho.

![Dashboard Geral](assets/analise-geral.png)
![Dashboard de Times](assets/analise-times.png)

---

## 🧪 Ciência de Dados & Teste de Hipóteses (EDA)

Não apenas mostramos o que aconteceu, mas **por que aconteceu**. Usamos análise exploratória avançada (EDA) para validar mitos do futebol:

=== "🏠 Hipótese 1: Declínio do Home Advantage"
    Muitos analistas sugerem que a vantagem de jogar em casa está diminuindo devido a gramados melhores, logística profissional e o VAR.

    ![Tendência Home Advantage](assets/home_advantage_regression.png)

    - **Insight Técnico:** O gráfico de regressão linear acima (gerado via `sns.regplot`) mostra a tendência real da taxa de vitória dos mandantes ao longo das décadas. 
    - **Conclusão:** O "fator casa" ainda existe, mas os dados mostram uma inclinação negativa sutil, sugerindo que o campeonato está se tornando mais equilibrado e menos dependente do estádio.

=== "🥅 Hipótese 2: O Teto de Gols"
    Analisamos como o volume total de gols de uma partida se distribui conforme o resultado final (Mandante vence, Visitante vence ou Empate).

    ![Distribuição de Gols](assets/goals_distribution_result.png)

    - **Observação:** Partidas que terminam em **Empate** possuem uma concentração de gols significativamente menor (baixo desvio padrão), enquanto vitórias de visitantes costumam ocorrer em jogos de placares mais abertos e caóticos (maior dispersão no Boxplot).

=== "🎯 Hipótese 3: Eficiência Ofensiva"
    Será que marcar muitos gols garante um aproveitamento de pontos proporcional, ou o equilíbrio defensivo é mais importante?

    ![Correlação Ofensiva](assets/offensive_efficiency_correlation.png)

    - **Análise Correlacional:** Existe uma correlação forte (R²) entre a média de gols marcados e a média de pontos ganhos. Times que mantêm média > 1.5 gols em casa (eixo X) raramente ficam fora das zonas de elite em aproveitamento (eixo Y).

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia |
| :--- | :--- |
| **Linguagem Base** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Manipulação** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) |
| **Visualização BI** | ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black) |
| **Estilo do Site** | ![MkDocs](https://img.shields.io/badge/MkDocs-Material-526CFE?style=flat&logo=materialformkdocs&logoColor=white) |

---

## 📈 Modelagem de Dados (Star Schema)

Para garantir que o Dashboard responda em milissegundos, implementamos uma arquitetura de dados otimizada:

![Modelagem de Dados](assets/modelagem-dados.png)

---
*Este repositório é um laboratório vivo de técnicas de BI e Data Science aplicadas ao esporte.*
