import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurações de estilo
plt.style.use('dark_background')
sns.set_theme(style="darkgrid", rc={"axes.facecolor": "#1e1e1e", "figure.facecolor": "#121212"})

input_file = "brasileirao_clean.csv"
assets_path = "docs/assets"

os.makedirs(assets_path, exist_ok=True)

def run_advanced_eda():
    if not os.path.exists(input_file):
        print(f"❌ Erro: {input_file} não encontrado.")
        return

    print(f"📈 Iniciando EDA Avançada: {input_file}...")
    df = pd.read_csv(input_file)
    df['data'] = pd.to_datetime(df['data'])
    df['ano'] = df['data'].dt.year
    
    # 1. Home Advantage Trend (Regressão)
    home_adv_yearly = df.groupby('ano').apply(lambda x: (x['vencedor'] == x['mandante']).mean()).reset_index(name='taxa_vitoria_home')
    plt.figure(figsize=(12, 6))
    sns.regplot(data=home_adv_yearly, x='ano', y='taxa_vitoria_home', color='#00ffcc', line_kws={"color": "red"})
    plt.title('Tendência Histórica: O Declínio do Mando de Campo?', fontsize=14, color='#00ffcc')
    plt.savefig(os.path.join(assets_path, "home_advantage_regression.png"))
    plt.close()

    # 2. Distribuição de Gols por Resultado
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='vencedor_local', y='total_gols', palette="viridis")
    plt.title('Volume de Gols vs. Tipo de Resultado', fontsize=12, color='#00ffcc')
    plt.savefig(os.path.join(assets_path, "goals_distribution_result.png"))
    plt.close()

    # 3. Eficiência Ofensiva
    equipes_stats = df.groupby('mandante').agg({'pontos_mandante': 'mean', 'mandante_placar': 'mean'}).rename(columns={'pontos_mandante': 'media_pontos', 'mandante_placar': 'media_gols_pro'})
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=equipes_stats, x='media_gols_pro', y='media_pontos', hue='media_pontos', palette='magma', size='media_pontos', sizes=(50, 400))
    plt.title('Correlação: Média de Gols vs. Aproveitamento em Casa', fontsize=12, color='#00ffcc')
    plt.savefig(os.path.join(assets_path, "offensive_efficiency_correlation.png"))
    plt.close()

    print("✅ Gráficos gerados com sucesso.")

if __name__ == "__main__":
    run_advanced_eda()
