import pandas as pd
import os

# Caminho dos arquivos
base_path = "analise-campeonato-brasileiro"
input_file = os.path.join(base_path, "brasileirao_clean.csv")

def run_eda():
    if not os.path.exists(input_file):
        print("❌ Arquivo limpo não encontrado. Execute o data_cleaning.py primeiro.")
        return

    df = pd.read_csv(input_file)
    df['data'] = pd.to_datetime(df['data'])
    df['ano'] = df['data'].dt.year

    print("\n--- ⚽ INSIGHTS DA ANÁLISE EXPLORATÓRIA (PANDAS) ---")

    # 1. Melhores Mandantes (Média de pontos por jogo em casa)
    mandantes = df.groupby('mandante')['pontos_mandante'].mean().sort_values(ascending=False).head(5)
    print("\n🏠 Top 5 Mandantes Históricos (Média de Pontos):")
    print(mandantes)

    # 2. Eficiência por Formação (Média de vitórias por formação)
    formacao_eficiencia = df[df['formacao_mandante'] != 'Não Informado'].groupby('formacao_mandante')['pontos_mandante'].mean().sort_values(ascending=False).head(5)
    print("\n📋 Top 5 Formações Táticas mais Eficientes (Mandante):")
    print(formacao_eficiencia)

    # 3. Evolução de Gols ao longo dos anos
    gols_por_ano = df.groupby('ano')['total_gols'].mean()
    print("\n📊 Média de Gols por Partida por Temporada:")
    print(gols_por_ano.tail(5))

    return gols_por_ano

if __name__ == "__main__":
    run_eda()
