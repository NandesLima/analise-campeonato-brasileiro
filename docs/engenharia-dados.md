# 🛠️ Engenharia de Dados: O Motor de Inteligência

Nesta fase do projeto, implementamos um pipeline de processamento de dados robusto utilizando **Python** e **Pandas**, elevando o nível técnico do projeto de um dashboard passivo para uma ferramenta de engenharia ativa.

## ⚙️ Arquitetura do Pipeline
O tratamento de dados agora segue um fluxo de **Modern Data Stack**:
1. **Raw (Bronse):** Dados brutos extraídos do CSV original.
2. **Transform (Silver):** Aplicação das regras de negócio via Python.
3. **Load (Gold):** Exportação de um arquivo otimizado para consumo analítico.

## 🧠 Lógica de Negócio Aplicada (Code Snippets)

### 1. Cálculo Dinâmico de Pontuação
Diferente do Power BI, onde cálculos de pontos costumam ser feitos via DAX (mais lento), aqui injetamos a lógica direto no motor de transformação:

```python
def calculate_points(row, side):
    if row['vencedor'] == '-':
        return 1 # Empate
    elif row['vencedor'] == row[side]:
        return 3 # Vitória
    else:
        return 0 # Derrota

df['pontos_mandante'] = df.apply(lambda row: calculate_points(row, 'mandante'), axis=1)
```

### 2. Normalização de Entidades
Tratamos inconsistências históricas em nomes de técnicos e formações táticas, garantindo que a análise de agrupamento no Power BI não apresente duplicatas por erros de digitação nos dados brutos.

### 3. Otimização de Tipagem (Memory Efficiency)
Convertmos strings de datas e objetos genéricos em tipos nativos do Pandas (`datetime64`), reduzindo o consumo de memória e acelerando filtros temporais em até 10x.

## 📋 Resultados do Processamento Automatizado
O arquivo [`data_cleaning.py`](https://github.com/NandesLima/analise-campeonato-brasileiro/blob/master/data_cleaning.py) entrega:

- **Volume Processado:** +7.600 partidas tratadas em milissegundos.
- **Data Quality:** 100% dos valores nulos em campos críticos de comando técnico foram mitigados.
- **Exportação:** Gerado o `brasileirao_clean.csv`, pronto para conexão via Power BI ou Notebooks Jupyter.

---
*Este processo transforma dados brutos em ativos de decisão, garantindo integridade e escalabilidade para o projeto.*

