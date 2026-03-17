# 📊 Análise Estatística & EDA (Exploratory Data Analysis)

Nesta etapa, utilizamos Python para extrair insights que dashboards convencionais muitas vezes não conseguem evidenciar de forma nativa. O foco é entender os padrões de comportamento do futebol brasileiro ao longo das décadas.

## ⚽ Evolução da Média de Gols (2003 - 2021)

Utilizamos o Python para calcular a média de gols marcados por partida em cada temporada. O gráfico abaixo revela a evolução da "competitividade" ou "postura defensiva" dos times ao longo de quase duas décadas.

![Evolução de Gols](assets/evolucao-gols.png)

### 🧠 Lógica de Análise (Insight Técnico)
O script [`eda_brasileirao.py`](https://github.com/NandesLima/analise-campeonato-brasileiro/blob/master/eda_brasileirao.py) realiza um agrupamento temporal (`groupby('ano')`) e extrai as médias móveis para suavizar flutuações sazonais, destacando tendências reais de performance ofensiva.

## 🏠 O Fator "Mando de Campo"
Quantificamos o peso real de jogar em casa. 

```python
vitorias_mandante = (df['vencedor'] == df['mandante']).mean()
print(f"Taxa de Vitória do Mandante: {vitorias_mandante:.2%}")
```

- **Análise Correlacional:** Através do EDA, identificamos que o mando de campo representa uma vantagem estatística de ~15% na probabilidade de vitória, um insight crucial para modelos preditivos.

## 🔝 Performance dos Clubes
Ranking de aproveitamento histórico baseado em pontos reais calculados, permitindo uma visão de longevidade e consistência de cada equipe na elite do futebol nacional.

---
*A análise exploratória serve como bússola para a criação de dashboards mais inteligentes no Power BI, focando no que realmente importa.*

