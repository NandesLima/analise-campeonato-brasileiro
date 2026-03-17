import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Caminhos
input_file = "analise-campeonato-brasileiro/brasileirao_clean.csv"
output_image = "analise-campeonato-brasileiro/docs/assets/evolucao-gols.png"

def generate_charts():
    if not os.path.exists(input_file):
        print("❌ Arquivo limpo não encontrado.")
        return

    # Configuração de estilo Neon/Dark para combinar com o portfólio
    plt.style.use('dark_background')
    df = pd.read_csv(input_file)
    df['data'] = pd.to_datetime(df['data'])
    df['ano'] = df['data'].dt.year

    # Agrupamento: Média de gols por ano
    gols_por_ano = df.groupby('ano')['total_gols'].mean().reset_index()

    # Criando o gráfico
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=gols_por_ano, x='ano', y='total_gols', marker='o', color='#00f2ff', linewidth=2.5)
    
    # Customização
    plt.title('⚽ Evolução da Média de Gols por Temporada (2003 - 2021)', fontsize=16, color='#00f2ff', pad=20)
    plt.xlabel('Temporada (Ano)', fontsize=12)
    plt.ylabel('Média de Gols por Partida', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()

    # Salvar a imagem
    plt.savefig(output_image, dpi=300)
    print(f"✅ Gráfico salvo com sucesso em: {output_image}")

if __name__ == "__main__":
    generate_charts()
